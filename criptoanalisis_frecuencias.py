msg = \
"RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE" + \
"AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE." + \
"AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ" + \
"TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX" + \
"DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936," + \
"PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN" + \
"TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE," + \
"HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK" + \
"HKCZJOI OKEJSZCNHE.\n"

print(msg, "\n")

frecuencias = dict()
for c in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
	frecuencias[c] = 0

for c in msg:
	if c in frecuencias:
		frecuencias[c] += 1

total = 0
for f in frecuencias:
	total += frecuencias[f]

def frecuencia(f):
	return f[1]
frecuencias = dict(reversed(sorted(frecuencias.items(), key=frecuencia)))

print("Frecuencias:")
for f in frecuencias:
	print(f, frecuencias[f] / total)

frecuencias_es = {
	'e': 16.78, 'a': 11.96, 'o': 8.69, 'l': 8.37, 's': 7.88, 'n': 7.01, 'd': 6.87,
    'r': 4.94, 'u': 4.80, 'i': 4.15, 't': 3.31, 'c': 2.92, 'p': 2.776, 'm': 2.12,
    'y': 1.54, 'q': 1.53, 'b': 0.92, 'h': 0.89, 'g': 0.73, 'f': 0.52, 'j': 0.30,
    'ñ': 0.29, 'z': 0.15, 'x': 0.06, 'k': 0.00, 'w': 0.00
}

msg_nuevo = msg
msg_nuevo = msg_nuevo.replace(list(frecuencias)[0], list(frecuencias_es)[0].lower())
msg_nuevo = msg_nuevo.replace(list(frecuencias)[1], list(frecuencias_es)[1].lower())
print("Mensaje original: ")
print(msg)
print("Mensaje alterado:")
print(msg_nuevo)

while True:
	c1 = input("Caracter a reemplazar: ")[0]
	c2 = input("Sustitución " + c1 + " : ")[0]
	c2 = c2.lower()
	msg_nuevo = msg_nuevo.replace(c1, c2)
	
	print("Frecuencias:")
	for f in frecuencias:
		print(f, frecuencias[f] / total)
	print("\nFrecuencias español:")
	for f in frecuencias_es:
		print(f, frecuencias_es[f])
	print("Original: ")
	print(msg)
	print("Modificado: ")
	print(msg_nuevo)
