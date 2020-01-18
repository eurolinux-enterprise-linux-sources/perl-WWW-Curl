Name:           perl-WWW-Curl
Version:        4.15
Release:        13%{?dist}
Summary:        Perl extension interface for libcurl
License:        MPLv1.1 or MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WWW-Curl/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SZ/SZBALINT/WWW-Curl-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
# Test::Pod is optional
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  libcurl-devel
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
%setup -q -n WWW-Curl-%{version}

# Remove bundled modules
rm -rf inc/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# These tests require network, use "--with network_tests" to execute them
%{?!_with_network_tests: rm t/01basic.t }
%{?!_with_network_tests: rm t/02callbacks.t }
%{?!_with_network_tests: rm t/04abort-test.t }
%{?!_with_network_tests: rm t/05progress.t }
%{?!_with_network_tests: rm t/08ssl.t }
%{?!_with_network_tests: rm t/09times.t }
%{?!_with_network_tests: rm t/14duphandle.t }
%{?!_with_network_tests: rm t/15duphandle-callback.t }
%{?!_with_network_tests: rm t/18twinhandles.t }
%{?!_with_network_tests: rm t/19multi.t }
%{?!_with_network_tests: rm t/21write-to-scalar.t }
make test

%files
%doc Changes LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/WWW*
%{_mandir}/man3/*

%changelog
* Wed Apr 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.15-13
- Rebuild to fetch the symbol from curl for TLS > 1.0 (bug #1445309)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.15-12
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.15-11
- Mass rebuild 2013-12-27

* Sun Jul 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 4.15-10
- Update dependencies
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Remove buildroot cleaning

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Jitka Plesnikova <jplesnik@redhat.com> - 4.15-8
- Specify all dependencies
- Modernize spec file

* Wed Aug 15 2012 Daniel Mach <dmach@redhat.com> - 4.15-7.1
- Rebuild for perl 5.16

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 4.15-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Iain Arnell <iarnell@gmail.com> 4.15-4
- use perl_default_filter

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.15-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.15-1
- Update to 4.15
* Thu Oct 28 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.14-1
- Update to 4.14
- Add a filter provide to avoid private-shared-object-provides error
* Sun Sep  5 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.13-1
- Update to 4.13
* Wed Aug 25 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.12-1
- Update to 4.12
* Thu Jun  3 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.11-3
- Remove test 19 because it requires network
* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.11-2
- Mass rebuild with perl-5.12.0
* Fri Dec 18 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.11-1
- Update to 4.11
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4.09-3
- rebuild against perl 5.10.1
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Sat Jul 11 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.09-1
- Rebuild for 4.09
* Mon Jun  1 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.07-1
- Rebuild for 4.07
* Sat Apr 18 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.06-1
- Step to 4.06
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-4
- Licence update
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-3
- README.Win32 file removed
* Wed Jan 14 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-2
- Timestamp preserved
- changelog format fix
- README.Win32 file removed
* Thu Dec 11 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 4.05-1
- Initial build with cpan2spec
