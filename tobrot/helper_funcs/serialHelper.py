import os
from tobrot.helper_funcs.download import download_tg
from datetime import date, datetime
import numpy as np
from tobrot.helper_funcs.upload_to_tg import upload_to_gdrive


async def anu_fn(client, message):
    user_id = message.from_user.id
    file, mess_age = await download_tg(client, message)
    start_date = date(2021, 9, 1)
    start_serial_no = 356
    today = date.today()
    total_days = (today - start_date).days
    sundays = int(np.busday_count(start_date, today, weekmask='Sun'))
    working_days = total_days - sundays
    today_serial_no = start_serial_no + working_days
    serial_name = f"E{today_serial_no} {today.day} {datetime.strptime(str(today.month), '%m').strftime('%B')}.mp4"
    if file:
        os.rename(file, serial_name)
    else:
        return
    await upload_to_gdrive(serial_name, mess_age, message, user_id, is_anu=True)
