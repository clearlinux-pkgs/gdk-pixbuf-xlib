#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdk-pixbuf-xlib
Version  : 2.40.2
Release  : 2
URL      : https://download.gnome.org/sources/gdk-pixbuf-xlib/2.40/gdk-pixbuf-xlib-2.40.2.tar.xz
Source0  : https://download.gnome.org/sources/gdk-pixbuf-xlib/2.40/gdk-pixbuf-xlib-2.40.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: gdk-pixbuf-xlib-lib = %{version}-%{release}
Requires: gdk-pixbuf-xlib-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson

%description
GdkPixbuf-Xlib
==============
GdkPixbuf-Xlib contains the deprecated API for integrating GdkPixbuf with
Xlib data types.

%package dev
Summary: dev components for the gdk-pixbuf-xlib package.
Group: Development
Requires: gdk-pixbuf-xlib-lib = %{version}-%{release}
Provides: gdk-pixbuf-xlib-devel = %{version}-%{release}
Requires: gdk-pixbuf-xlib = %{version}-%{release}

%description dev
dev components for the gdk-pixbuf-xlib package.


%package lib
Summary: lib components for the gdk-pixbuf-xlib package.
Group: Libraries
Requires: gdk-pixbuf-xlib-license = %{version}-%{release}

%description lib
lib components for the gdk-pixbuf-xlib package.


%package license
Summary: license components for the gdk-pixbuf-xlib package.
Group: Default

%description license
license components for the gdk-pixbuf-xlib package.


%prep
%setup -q -n gdk-pixbuf-xlib-2.40.2
cd %{_builddir}/gdk-pixbuf-xlib-2.40.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607488760
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gdk-pixbuf-xlib
cp %{_builddir}/gdk-pixbuf-xlib-2.40.2/COPYING %{buildroot}/usr/share/package-licenses/gdk-pixbuf-xlib/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlib.h
/usr/include/gdk-pixbuf-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlibrgb.h
/usr/lib64/libgdk_pixbuf_xlib-2.0.so
/usr/lib64/pkgconfig/gdk-pixbuf-xlib-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdk_pixbuf_xlib-2.0.so.0
/usr/lib64/libgdk_pixbuf_xlib-2.0.so.0.4000.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gdk-pixbuf-xlib/01a6b4bf79aca9b556822601186afab86e8c4fbf
