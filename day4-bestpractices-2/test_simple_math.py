import simple_math

def test_simple_add():
	assert simple_math.simple_add(8.89, 7.054) == 15.944

def test_simple_sub():
	assert simple_math.simple_sub(8, 1) == 7

def test_simple_mult():
	assert simple_math.simple_mult(8, 7) == 56

def test_simple_div():
	assert simple_math.simple_div(9, 3) == 3

def test_poly_first():
	assert simple_math.poly_first(1, 1, 1) == 2
