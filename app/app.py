from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
#import the PostCreate schema
from app.schemas import PostCreate, PostResponse 
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield



app = FastAPI(lifespan=lifespan)


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session)
):
    post = Post(
        caption=caption,
        url="dummy url",
        file_type="photo",
        file_name="dummy name"
    )

    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post 

#Feed
@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    #this query the data from the database
    #select from the post, then you have the filter ordered by descending.

    #Prepare for the frontend
    posts_data = []
    for post in posts:
        #create a more response post on the frontend
        posts_data.append(
            {
                "id": str(post.id),
                "caption":post.caption,
                "url":post.url,
                "file_type":post.file_type,
                "file_name":post.created_at.isoformat(),
                "created_ad":post.created_at.isoformat()
            }
        )
    return {"posts": posts_data}
    

# # #Hello World
# # @app.get("/hello-world")
# # def hello_world():
# #     #JSON => Javascript 
# #     return {"message": "Hello World"}



# text_posts = {
#     1: {"title": "The Beauty of Morning Routines", "content": "Starting your day with small, intentional habits can set the tone for everything that follows."},
#     2: {"title": "Why Learning Never Ends", "content": "Education doesn’t stop after school — every experience is an opportunity to grow."},
#     3: {"title": "The Power of Minimalism", "content": "Owning less helps you focus on what truly matters — people, purpose, and peace of mind."},
#     4: {"title": "Balancing Work and Rest", "content": "Hustle culture glorifies burnout, but rest is a necessary part of long-term success."},
#     5: {"title": "How to Build Consistency", "content": "Start small, stay steady, and trust that progress compounds over time."},
#     6: {"title": "Creativity in Everyday Life", "content": "You don’t have to be an artist to create — creativity thrives in problem-solving and expression."},
#     7: {"title": "Overcoming Fear of Failure", "content": "Failure is not the opposite of success — it’s the pathway to mastering your craft."},
#     8: {"title": "Digital Detox: A Modern Necessity", "content": "Disconnecting from screens helps reconnect with yourself and the world around you."},
#     9: {"title": "The Importance of Gratitude", "content": "Practicing gratitude daily can shift your mindset from scarcity to abundance."},
#     10: {"title": "Finding Joy in Small Moments", "content": "Happiness often hides in the simplest things — a laugh, a sunset, a shared meal."}
# }

# # text_posts = {1:{"title": "New Post", "content": "cool test post"}}

# #GET
# @app.get("/posts")
# def get_all_posts(limit: int = None):
#     if limit:
#         return list(text_posts.values())[:limit]
#     return text_posts

# @app.get("/posts/{id}")
# def get_post(id:int)-> PostResponse:
#     if id not in text_posts:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return text_posts.get(id)


# #POST
# @app.post("/posts")
# def create_post(post: PostCreate)-> PostResponse:
#     new_post = {"title": post.title, "content": post.content}
#     text_posts[max(text_posts.keys()) + 1] = new_post
#     return new_post

# #DELETE
# @app.delete("/posts/{id}")
# def delete_post(post_id):
#     pass



# #Query parameters


