from app.core.base.email import BaseEmailSender
from app.utils.email_context import USER_VERIFY_ACCOUNT, FORGOT_PASSWORD

class SendAccountVerificationEmail(BaseEmailSender):
    async def send(self):
        string_context = self.user.get_context_string(USER_VERIFY_ACCOUNT)
        token = string_context # it should be hashed
        activate_url = f"{self.fronted_host}/auth/account-verify?token={token}&email={self.user.email}"
        data = {
            'app_name': self.app_name,
            'name': self.user.last_name,
            'activate_url': activate_url
        }
        subject = f"Account Verification - {self.app_name}"
        await self.send_email(subject, data, "user/account-verification.html")

class SendAccountActivationConfirmationEmail(BaseEmailSender):
    async def send(self):
        data = {
            'app_name': self.app_name,
            'name': self.user.last_name,
            'login_url': self.fronted_host
        }
        subject = f"Welcome - {self.app_name}"
        await self.send_email(subject, data, "user/account-verification-confirmation.html")

class SendPasswordResetEmail(BaseEmailSender):
    async def send(self):
        string_context = f"{self.user.get_context_string(FORGOT_PASSWORD)}"
        token = string_context # hash this token
        reset_url = f"{self.fronted_host}/reset-password?token={token}&email={self.user.email}"
        data = {
            'app_name': self.app_name,
            'name': self.user.last_name,
            'activate_url': reset_url
        }
        subject = f"Reset Password - {self.app_name}"
        await self.send_email(subject, data, "user/password-reset.html")