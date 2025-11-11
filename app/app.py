from fastapi import FastAPI, HTTPException
#import the PostCreate schema
from app.schemas import PostCreate




app = FastAPI()

# #Hello World
# @app.get("/hello-world")
# def hello_world():
#     #JSON => Javascript 
#     return {"message": "Hello World"}



text_posts = {
    {"title": "The Beauty of Morning Routines", "content": "Starting your day with small, intentional habits can set the tone for everything that follows."},
    {"title": "Why Learning Never Ends", "content": "Education doesn’t stop after school — every experience is an opportunity to grow."},
    {"title": "The Power of Minimalism", "content": "Owning less helps you focus on what truly matters — people, purpose, and peace of mind."},
    {"title": "Balancing Work and Rest", "content": "Hustle culture glorifies burnout, but rest is a necessary part of long-term success."},
    {"title": "How to Build Consistency", "content": "Start small, stay steady, and trust that progress compounds over time."},
    {"title": "Creativity in Everyday Life", "content": "You don’t have to be an artist to create — creativity thrives in problem-solving and expression."},
    {"title": "Overcoming Fear of Failure", "content": "Failure is not the opposite of success — it’s the pathway to mastering your craft."},
    {"title": "Digital Detox: A Modern Necessity", "content": "Disconnecting from screens helps reconnect with yourself and the world around you."},
    {"title": "The Importance of Gratitude", "content": "Practicing gratitude daily can shift your mindset from scarcity to abundance."},
    {"title": "Finding Joy in Small Moments", "content": "Happiness often hides in the simplest things — a laugh, a sunset, a shared meal."}
}

# text_posts = {1:{"title": "New Post", "content": "cool test post"}}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def _get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post


#Query parameters


