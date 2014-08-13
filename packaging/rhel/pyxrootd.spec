%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global _binaries_in_noarch_packages_terminate_build 0

%global __os_install_post    \
    /usr/lib/rpm/redhat/brp-compress \
    %{!?__debug_package:/usr/lib/rpm/redhat/brp-strip %{__strip}} \
    /usr/lib/rpm/redhat/brp-strip-static-archive %{__strip} \
    /usr/lib/rpm/redhat/brp-strip-comment-note %{__strip} %{__objdump} \
    /usr/lib/rpm/redhat/brp-java-repack-jars \
%{nil}

Name:           xrootd-python
Version:        0.1.3
Release:        2.CERN%{?dist}
License:        GPL3
Summary:        Python bindings for XRootD
Group:          Development/Tools
Packager:       XRootD Developers <xrootd-dev@slac.stanford.edu>
URL:            http://github.com/xrootd/python-xrootd
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       python >= 2.4
Requires:       xrootd-client >= 3.3.3
BuildRequires:  xrootd-client-devel python-devel

%description
pyxrootd is a set of python language bindings for xrootd.

%prep
%setup -n %{name}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
[ "x%{buildroot}" != "x/" ] && rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Thu Nov 28 2013 Lukasz Janyst <ljanyst@cern.ch>
- Tag 0.1.3
* Tue Jul 01 2013 Justin Salmon <jsalmon@cern.ch>
- Tag version 0.1.2
* Tue Jul 01 2013 Justin Salmon <jsalmon@cern.ch>
- Depend on updated new client package name
  (xrootd-client)
* Tue May 14 2013 Justin Salmon <jsalmon@cern.ch>
- Tag version 0.1.1
* Fri Apr 26 2013 Justin Salmon <jsalmon@cern.ch>
- Tag version 0.1.0
* Fri Apr 26 2013 Justin Salmon <jsalmon@cern.ch>
- Add requirement for xrootd-cl 3.3.2
* Fri Apr 26 2013 Justin Salmon <jsalmon@cern.ch>
- Install to correct place in RHEL5
* Wed Apr 03 2013 Justin Salmon <jsalmon@cern.ch>
- Initial version

