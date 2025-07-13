from pygfx.renderers.wgpu.shader.templating import apply_templating
import numpy as np

numpy_array = np.random.rand(2, 3, 4)


fixed_shape_code = """
const DCT_BASIS: array<array<array<f32, 4>, 3>, 2> = array(
    $$ for basis_index in range(2)
        array(
        $$ for i in range(3)
            array(
            $$ for j in range(4)
                {{ arr[basis_index, i, j] }},
            $$ endfor
            )
        $$ endfor
        )
    $$ endfor
    )
"""

dynamic_shape_code = """
const DCT_BASIS: array<array<array<f32, {{ arr.shape[2] }}>, {{ arr.shape[1] }}>, {{ arr.shape[0] }}> = array(
    $$ for basis_index in range(arr.shape[0])
        array(
        $$ for i in range(arr.shape[1])
            array(
            $$ for j in range(arr.shape[2])
                {{ arr[basis_index, i, j] }},
            $$ endfor
            )
        $$ endfor
        )
    $$ endfor
    )
"""


values = {
    "arr": numpy_array
}

print("*** fixed shape ***")
print(apply_templating(fixed_shape_code, **values))

print("\n\n*** dynamic shape ***")
print(apply_templating(dynamic_shape_code, **values))
