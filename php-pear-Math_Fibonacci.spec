%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Fibonacci
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Package to calculat and manipulate Fibonacci numbers
Summary(pl):	%{_class}_%{_subclass} - pakiet do obliczania i manipulowania na liczbach Fibonacciego
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	2.1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	924091a540df8d7fe2a7f37996223fa8
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Math_Fibonacci/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fibonacci series is constructed using the formula:
F(n) = F(n - 1) + F(n - 2),
By convention F(0) = 0, and F(1) = 1.
An alternative formula that uses the Golden Ratio can also be used:
F(n) = (PHI^n - phi^n)/sqrt(5) [Lucas' formula],
where PHI = (1 + sqrt(5))/2 is the Golden Ratio, and phi = (1 - sqrt(5))/2
is its reciprocal.

Requires Math_Integer, and can be used with big integers if the GMP or
the BCMATH libraries are present.

In PEAR status of this package is: %{_status}.

%description -l pl
Ci±g Fibonacciego jest skonstruowany wed³ug wzoru:
F(n) = F(n - 1) + F(n - 2).
Z za³o¿enia F(0) = 0 oraz F(1) = 1.
Mo¿na równie¿ u¿yæ alternatywnego wzoru, wykorzystuj±cego wspó³czynnik
z³otego podzia³u:
F(n) = (PHI^n - phi^n)/sqrt(5)  [wzór Lucasa]
gdzie PHI = (1 + sqrt(5))/2 jest wspó³czynnikiem z³otego podzia³u, a
phi = (1 - sqrt(5))/2 jego odwrotno¶ci±.

Klasa wymaga pakietu Math_Integer, mo¿e byæ u¿ywana dla du¿ych liczb
je¶li zainstalowany jest modu³ GMP lub BCMATH.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/test/*,tests/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
