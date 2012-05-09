Name:           fedora-bookmarks
Version:        15
Release:        0.2
Summary:        Fedora bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://fedoraproject.org/
# I had to strip the embedded icons out of the bookmarks file, because they are not 
# distributable under the GFDL. See https://bugzilla.redhat.com/show_bug.cgi?id=433471
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for Fedora.

%prep
# We are nihilists, Lebowski.  We believe in nassing.

%build
# We are nihilists, Lebowski.  We believe in nassing.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 16 2011 Nick Bebout <nb@fedoraproject.org> 15-0.1
- Change release notes to just link to Fedora Documentation

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 22 2010 Christopher Aillon <caillon@redhat.com> 13-1
- Minor updates from marketing

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  1 2009 Christopher Aillon <caillon@redhat.com> - 11-1
- Refresh Fedora Project link set
- Add new Free Content link
- Remove obsolete links

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> 10-1
- fix bookmarks.html to not have embedded icons, they aren't usable under the GFDL.
  resolves bz 433471

* Wed Oct 17 2007 Matthias Clasen <mclasen@redhat.com> 8-1
- Update the link to the Fedora project homepage  (#291851)

* Tue Oct  2 2007 Matthias Clasen <mclasen@redhat.com> 7-2
- Remove reference to 'Core' from summary.  (#247362)

* Sun Apr 15 2007 Christopher Aillon <caillon@redhat.com> 7-1
- FC7 bookmarks based on http://fedoraproject.org/wiki/Releases/7/Bookmarks

* Tue Mar 20 2007 Christopher Aillon <caillon@redhat.com> 6-2
- Package review updates

* Wed Oct 18 2006 Christopher Aillon <caillon@redhat.com> 6-1
- Initial version

