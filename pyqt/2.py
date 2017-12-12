import time
import datetime

# utc 转 local
def utc2local(utc_st):
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st
# local 转 utc
def local2utc(local_st):
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st

utc_time = datetime.datetime(2014, 9, 18, 10, 42, 16, 126000)
local_time = utc2local(utc_time)
print (local_time.strftime("%Y-%m-%d %H:%M:%S"))
# output：2014-09-18 18:42:16