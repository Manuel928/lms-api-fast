import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def create_course_api():
    return {"Courses": {}}


@router.post("/courses/{id}")
async def read_course():
    return {"Courses": {}}


@router.get("/courses/{id}")
async def update_course():
    return {"Courses": {}}


@router.patch("/courses/{id}")
async def delete_courses():
    return {"Courses": {}}


@router.delete("/courses/{id}")
async def read_courses():
    return {"Courses": {}}
