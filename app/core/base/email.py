from fastapi import BackgroundTasks

from app.v1.models.user import User
from app.core.config.email import send_email
from app.utils.settings import settings

class BaseEmailSender:
    def __init__(self, user: User, background_tasks: BackgroundTasks):
        self.user = user
        self.background_tasks = background_tasks
        self.app_name = settings.APP_NAME
        self.fronted_host = settings.FRONTEND_URL

    async def send_email(self, subject, context, template_name):
        await send_email(
            recipients=[self.user.email],
            subject=subject,
            template_name=template_name,
            context=context,
            background_tasks=self.background_tasks
        )
