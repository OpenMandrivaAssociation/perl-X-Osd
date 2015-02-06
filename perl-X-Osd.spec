%define module X-Osd

Summary:	Perl5 modules for xosd
Name:		perl-%{module}
Version:	0.7
Release:	17
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/G/GO/GOZER/%{module}-%{version}.tar.bz2
Requires:	perl 
BuildRequires:	xosd-devel, perl-devel

%description
Perl extension to the X On Screen Display library (xosd)

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std 

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/*/*

%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.7-14mdv2012.0
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.7-13mdv2010.0
+ Revision: 430669
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.7-12mdv2009.0
+ Revision: 258885
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.7-11mdv2009.0
+ Revision: 246791
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.7-9mdv2008.1
+ Revision: 151400
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-8mdv2008.0
+ Revision: 87077
- rebuild


* Thu Jun 22 2006 Erwan Velu <erwan@seanodes.com> 0.7-7
- Rebuild

* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 0.7-6mdk
- Fixing source path

* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 0.7-5mdk
- Cleaning spec

* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 0.7-4mdk
- Rebuild

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.7-3mdk 
- rebuild for new perl
- fix spec name

* Tue Jun 22 2004 Michael Scherer <misc@mandrake.org> 0.7-2mdk 
- remove Requires on xosd, who turn out to pull xmms-xosd.

* Wed May 05 2004 Erwan Velu <erwan@mandrakesoft.com> 0.7-1mdk
- 0.7 (8 months in late :/)

