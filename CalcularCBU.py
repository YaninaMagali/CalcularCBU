
def convertir_a_tupla(bloque1):
	"""
	Este metodo recibe un string y lo convierte en una tupla de strings
	"""
	bloque1 = tuple(bloque1)
	return bloque1
	
	
def calcular_primer_digito_verificador(bloque1):
	"""
	Este metodo recibe una tupla y devuelve el dígito verificador del bloque 1
	"""
	bloque1 = convertir_a_tupla(bloque1)
	
	
	B1, B2, B3, S1, S2, S3, S4 = bloque1
	Suma1 = int(B1)*7 + int(B2)*1 + int(B3)*3 + int(S1)*9 + int(S2)*7 + int(S3)*1 + int(S4)*3
	
	Suma1_tuple = [int(x) for x in str(Suma1)]	
	
	digito_verificador_uno = 10 - Suma1_tuple[-1]
	return digito_verificador_uno


	
def calcular_segundo_digito_verificador(bloque2):
	bloque2 = convertir_a_tupla(bloque2)
	
	C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13 = bloque2
	Suma2 = int(C1)*3 + int(C2)*9 + int(C3)*7 + int(C4)*1 + int(C5)*3 + int(C6)*9 + int(C7)*7 + int(C8)*1 + int(C9)*3 + int(C10)*9 + int(C11)*7 + int(C12)*1 + int(C13)*3
	
	Suma1_tuple = [int(x) for x in str(Suma2)]	
	
	digito_verificador_dos = 10 - Suma1_tuple[-1]
	return digito_verificador_dos
		
def calcular_cbu():
	"""
	Este metodo cacula el cbu, recibe dos parámetros: bloque1 y bloque2. 
	El 1er bloque contiene 8 dígitos distribuidos de la siguiente manera:
	• Banco (3 dígitos)
	• Sucursal (4 dígitos)
	• Dígito verificador de los primeros 7 dígitos (1 dígito)
	
	El 2do bloque contiene 14 dígitos distribuidos de la siguiente manera:
	• Cuenta (13 dígitos)
	• Dígito verificador de los anteriores 13 (1 dígito)
	"""

	bloque_1 = input('Enter bloque_1, compuesto por FIID del banco (3 dígitos) y sucursal (4 dígitos):')
	bloque_2 = input('Enter bloque_2, compuesto por el número de cuenta (13 dígitos):'​)

	uno = calcular_primer_digito_verificador(bloque_1)
	dos = calcular_segundo_digito_verificador(bloque_2)
	print('El CBU es:', bloque_1,uno, bloque_2,dos)


calcular_cbu()
