#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-hk2
Version  : 2.4.0.b34
Release  : 2
URL      : https://github.com/javaee/hk2/archive/2.4.0-b34.tar.gz
Source0  : https://github.com/javaee/hk2/archive/2.4.0-b34.tar.gz
Source1  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.jar
Source2  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.pom
Source3  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.jar
Source4  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.1 GPL-2.0
Requires: mvn-hk2-data = %{version}-%{release}

%description
DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
The contents of this file are subject to the terms of either the GNU
General Public License Version 2 only ("GPL") or the Common Development
and Distribution License("CDDL") (collectively, the "License").  You
may not use this file except in compliance with the License.  You can
obtain a copy of the License at
https://glassfish.dev.java.net/public/CDDL+GPL_1_1.html
or packager/legal/LICENSE.txt.  See the License for the specific
language governing permissions and limitations under the License.

%package data
Summary: data components for the mvn-hk2 package.
Group: Data

%description data
data components for the mvn-hk2 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.pom
