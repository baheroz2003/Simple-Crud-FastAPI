from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bson.objectid import ObjectId
from datetime import datetime
from database import notes_collection

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    notes = list(notes_collection.find().sort("created_at", -1))
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": notes}
    )


@app.post("/add")
async def add_note(title: str = Form(...), content: str = Form(...)):
    notes_collection.insert_one({
        "title": title,
        "content": content,
        "created_at": datetime.utcnow()
    })
    return RedirectResponse("/", status_code=303)


@app.get("/delete/{id}")
async def delete_note(id: str):
    notes_collection.delete_one({"_id": ObjectId(id)})
    return RedirectResponse("/", status_code=303)


@app.get("/edit/{id}", response_class=HTMLResponse)
async def edit_page(request: Request, id: str):
    note = notes_collection.find_one({"_id": ObjectId(id)})
    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "note": note}
    )


@app.post("/update/{id}")
async def update_note(id: str, title: str = Form(...), content: str = Form(...)):
    notes_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "title": title,
            "content": content,
            "updated_at": datetime.utcnow()
        }}
    )
    return RedirectResponse("/", status_code=303)
