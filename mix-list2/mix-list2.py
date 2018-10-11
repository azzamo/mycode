#!/usr/bin/env python3

proto = ['ssh', 'http', 'https']

print(proto)
print(proto[1])

# this line will add 'dns' to the end of our list
proto.extend('dns')
print(proto)

# this line will add 'dns' to the end of our list
proto.append('dns')
print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)

proto.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (proto)
