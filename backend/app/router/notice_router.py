from fastapi import APIRouter, HTTPException

from app.model.notice import NoticeCreate, NoticeUpdate
from app.service.notice_service import (
    create_notice,
    get_all_notices,
    get_notice_by_id,
    replace_notice,
    update_notice,
    delete_notice,
)

router = APIRouter(
    prefix="/notices",
    tags=["Notices"]
)


@router.post("/")
def create_new_notice(notice: NoticeCreate):
    return create_notice(notice)


@router.get("/")
def get_notices():
    return get_all_notices()


@router.get("/{notice_id}")
def get_notice(notice_id: str):
    notice = get_notice_by_id(notice_id)

    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    return notice


@router.put("/{notice_id}")
def replace_existing_notice(notice_id: str, notice: NoticeCreate):
    updated_notice = replace_notice(notice_id, notice)

    if not updated_notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    return updated_notice


@router.patch("/{notice_id}")
def update_existing_notice(notice_id: str, notice: NoticeUpdate):
    updated_notice = update_notice(notice_id, notice)

    if not updated_notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    return updated_notice


@router.delete("/{notice_id}")
def delete_existing_notice(notice_id: str):
    deleted = delete_notice(notice_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Notice not found")

    return {"message": "Notice deleted successfully"}