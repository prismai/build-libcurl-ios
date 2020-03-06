libcurl for iOS
=================
Build libcurl for iOS development.  
This script will generate static library for armv7 armv7s arm64 i386 and x86_64.  
Bitcode support.  
OpenSSL and Darwin native ssl support.  
  
Script only, please download libcurl from here: http://curl.haxx.se/download.html  
Tested Xcode 8.2.1 on macOS 10.12.4  
Tested curl 7.69.0

Usage
=================
```
curl -O https://curl.haxx.se/download/curl-7.69.0.tar.gz
tar xf curl-7.69.0.tar.gz
cd curl-7.69.0
......
```
Find the result libcurl-ios-dist on your desktop.

curl-7.52.1 issue
=================
7.52.1 is the latest release but have an issue to build with darwinssl

https://github.com/curl/curl/issues/1172

https://github.com/curl/curl/commit/8db3afe16c0916ea5acf6aed6e7cf02f06cc8677

The fix have commited to curl just one day after release, which should be avaliable for the next patch release.

Workaround for this issue is:
- patch it with the commit (See darwinssl-fix-iOS-build.patch extacted)
- Or, use openssl with:

```bash
../build_libcurl_dist.sh openssl
```

OpenSSL
=================
The script link with native ssl by default (--with-darwinssl).  
To use OpenSSL, use https://github.com/sinofool/build-openssl-ios/ to build OpenSSL for iOS first, in curl source directory run:

```bash
curl https://raw.githubusercontent.com/sinofool/build-libcurl-ios/master/build_libcurl_dist.sh openssl |bash
```

Binary 
=================
You can find a prebuild binary (version 7.57.0 built without OpenSSL) here: https://sinofool.net/dl/libcurl-ios-dist.tar.gz

Double check the binary file before use:

```
SHA1:
a94458b89ef18b90422cf3affbdac5b8e2e0a0fd  libcurl-ios-dist.tar.gz

GnuPG: (My Key ID: 9BE18853)
https://sinofool.net/dl/libcurl-ios-dist.tar.gz.sig
```
