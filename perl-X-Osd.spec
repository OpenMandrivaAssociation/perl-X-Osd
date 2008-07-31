%define module X-Osd
%define	version	0.7
%define release	%mkrel 12

Summary:  	Perl5 modules for xosd
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/G/GO/GOZER/%{module}-%{version}.tar.bz2
Requires:	perl 
BuildRequires:	xosd-devel, perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl extension to the X On Screen Display library (xosd)

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf %{buildroot}
%makeinstall_std 

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root) 
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/*/*

