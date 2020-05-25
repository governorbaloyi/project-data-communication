from ProcessUtil import ProcessUtil
from time import sleep

processUtil = ProcessUtil()

for i in range(4):
    sleep(2)
    processUtil.switch_on(i)

for i in range(4):
    sleep(2)
    processUtil.switch_off(i)