import requests

# La URL de tu microservicio corriendo en Docker
URL = "http://localhost:5000/multiplicar"

def pedir_multiplicacion(n1, n2):
    params = {'a': n1, 'b': n2}
    try:
        response = requests.get(URL, params=params)
        if response.status_code == 200:
            datos = response.json()
            print(f"✅ El microservicio dice: {datos['a']} x {datos['b']} = {datos['resultado']}")
        else:
            print(f"❌ Error: {response.json()['error']}")
    except Exception as e:
        print(f"🔌 No se pudo conectar al microservicio: {e}")

if __name__ == '__main__':
    print("--- Cliente del Microservicio ---")
    num1 = input("Ingresa el primer número: ")
    num2 = input("Ingresa el segundo número: ")
    pedir_multiplicacion(num1, num2)

