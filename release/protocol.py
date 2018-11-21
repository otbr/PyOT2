def parseLookAt(net):
	x = net.getShort()
	y = net.getShort()
	z = net.getByte()
	spriteid = net.getShort()
	stack = net.getByte()
