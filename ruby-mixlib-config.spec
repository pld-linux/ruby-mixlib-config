#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	mixlib-config
Summary:	Simple ruby config mix-in
Name:		ruby-%{pkgname}
Version:	1.1.2
Release:	2
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	ecdbaec2ff60d572350b060f28848f0d
# Silence verbose test output. Fixed upstream in master but not yet released
# https://github.com/opscode/mixlib-config/commit/fa42def234f3a2d69229340733131b93a887be8d
Patch0:		mixlib-config-silence-tests.patch
URL:		http://github.com/opscode/mixlib-config
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class based config mix-in, similar to the one found in Chef.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q

%build
%__gem_helper spec

%if %{with tests}
rspec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc NOTICE
%{ruby_vendorlibdir}/mixlib/config.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

# FIXME, who owns the dir?
%dir %{ruby_vendorlibdir}/mixlib

%if 0
%files doc
%defattr(644,root,root,755)
%endif
