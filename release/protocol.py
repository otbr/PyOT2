def parseLookAt(net): # this is a demo to illustrate how /release works
	x = net.getShort()
	y = net.getShort()
	z = net.getByte()
	spriteid = net.getShort()
	stack = net.getByte()
