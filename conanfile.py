from conans import ConanFile, tools


class LibCurlConan(ConanFile):
    name = "libcurl"
    version = "7.69.0"
    settings = "os", "arch"

    def package(self):
        self.copy("*", dst="include", src="include")
        self.copy("*", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

