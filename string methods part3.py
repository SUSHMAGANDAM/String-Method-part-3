##format
# print("i want to this for rs.{f} or for rs{t}".format (f=15,t=15))
# l="r\tn\tk"
# print(l)
# print(l.expandtabs(0))
# print(l.expandtabs(1))
# print(l.expandtabs(2))
# print(l.expandtabs(3))
# print(l.expandtabs(4))
# print(l.expandtabs(5))
# print(l.expandtabs(6))
# print(l.expandtabs(7))
# print(l.expandtabs(8))
# print(l.expandtabs(9))
##maketrans and translate
# f="hello world"
# a=f.maketrans("l","e")
# print(f.translate(a))
# print(a)
# r={}
# print(type(r))
# s={3:"python","a":"hello"}
# print(type(s))
# print(s["a"],s[3])
##split lines
s="rama\nis\na\ngood\ngirl"
print(s)
print(type (s))
g=s.splitlines()
print(g,type(g))
print(g[1])
print(g[4])
h="hello welcome to josh python"
g=h.split()
print(g,type(g))
print(g[0])
print(g[1][:6])
# print(h.split(""))
print(h.split(" "))