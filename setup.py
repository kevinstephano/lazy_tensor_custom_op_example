from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension

ext_modules = []

ext_modules.append(
    CUDAExtension(
        name="lazy_tensor_custom_op",
        sources=[
            "csrc/multi_tensor_l2norm_kernel_mp.cu",
            "csrc/multi_tensor_lamb_mp.cu",
        ],
        extra_compile_args={
            "cxx": ["-O3"],
            "nvcc": 
                [
                    "-lineinfo",
                    "-O3",
                    "--use_fast_math",
                ]
        },
    )
)

setup(
    name="warp_perspective",
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension.with_options(no_python_abi_suffix=True)},
)
