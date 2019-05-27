# FollowSpot

Main programs are named "Follow_spot_KCf.ipynb" and "Follow_spot_exe_viola_jones.ipynb". First one uses different algoritems for following objects. We can modify which algorithm of given will we use. The second program is using face detection to follow human face with the spotlight. <br/><br/>
Then there is "Arduino_programcek_16-bit.ino", which receives data from python and sends it to SN75176A chip. This chip is a differential bus transceiver and converts signal from arduino to a signal that DMX understands. DMX signal is being used to drive spotlight and change settings on it.<br/><br/>
File named "Test_spremenjen.ui" is a GUI file, which can be opened and modified using PYQT5 designer. It has rough information about positions of buttons in GUI and so on.<br/><br/>
