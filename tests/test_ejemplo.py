import sys
import os

# Añadir el directorio src a sys.path para que pueda importar la función 'suma'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ejemplo import suma  # Importamos la función desde src/ejemplo.py

def test_suma():
    """Test que verifica si la función suma funciona correctamente."""
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
