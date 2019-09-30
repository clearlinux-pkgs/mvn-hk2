#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-hk2
Version  : 2.4.0.b34
Release  : 11
URL      : https://github.com/javaee/hk2/archive/2.4.0-b34.tar.gz
Source0  : https://github.com/javaee/hk2/archive/2.4.0-b34.tar.gz
Source1  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/2.4.0-b34/external-2.4.0-b34.pom
Source2  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/2.5.0/external-2.5.0.pom
Source3  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.jar
Source4  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.pom
Source5  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/aopalliance-repackaged/2.5.0/aopalliance-repackaged-2.5.0.jar
Source6  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/aopalliance-repackaged/2.5.0/aopalliance-repackaged-2.5.0.pom
Source7  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/jakarta.inject/2.5.0/jakarta.inject-2.5.0.jar
Source8  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/jakarta.inject/2.5.0/jakarta.inject-2.5.0.pom
Source9  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.jar
Source10  : https://repo1.maven.org/maven2/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.pom
Source11  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-api/2.4.0-b34/hk2-api-2.4.0-b34.jar
Source12  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-api/2.4.0-b34/hk2-api-2.4.0-b34.pom
Source13  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-api/2.5.0/hk2-api-2.5.0.jar
Source14  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-api/2.5.0/hk2-api-2.5.0.pom
Source15  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-bom/2.4.0-b34/hk2-bom-2.4.0-b34.pom
Source16  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-bom/2.5.0/hk2-bom-2.5.0.pom
Source17  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-locator/2.4.0-b34/hk2-locator-2.4.0-b34.jar
Source18  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-locator/2.4.0-b34/hk2-locator-2.4.0-b34.pom
Source19  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-locator/2.5.0/hk2-locator-2.5.0.jar
Source20  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-locator/2.5.0/hk2-locator-2.5.0.pom
Source21  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-parent/2.4.0-b34/hk2-parent-2.4.0-b34.pom
Source22  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-parent/2.5.0/hk2-parent-2.5.0.pom
Source23  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-utils/2.4.0-b34/hk2-utils-2.4.0-b34.jar
Source24  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-utils/2.4.0-b34/hk2-utils-2.4.0-b34.pom
Source25  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-utils/2.5.0/hk2-utils-2.5.0.jar
Source26  : https://repo1.maven.org/maven2/org/glassfish/hk2/hk2-utils/2.5.0/hk2-utils-2.5.0.pom
Source27  : https://repo1.maven.org/maven2/org/glassfish/pom/8/pom-8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.1 GPL-2.0
Requires: mvn-hk2-data = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

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
%setup -q -n hk2-2.4.0-b34

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/2.4.0-b34
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/2.4.0-b34/external-2.4.0-b34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/2.5.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/2.5.0/external-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.5.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.5.0/aopalliance-repackaged-2.5.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.5.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.5.0/aopalliance-repackaged-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/jakarta.inject/2.5.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/jakarta.inject/2.5.0/jakarta.inject-2.5.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/jakarta.inject/2.5.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/jakarta.inject/2.5.0/jakarta.inject-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.4.0-b34
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.4.0-b34/hk2-api-2.4.0-b34.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.4.0-b34
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.4.0-b34/hk2-api-2.4.0-b34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.5.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.5.0/hk2-api-2.5.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.5.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.5.0/hk2-api-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-bom/2.4.0-b34
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-bom/2.4.0-b34/hk2-bom-2.4.0-b34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-bom/2.5.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-bom/2.5.0/hk2-bom-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.4.0-b34
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.4.0-b34/hk2-locator-2.4.0-b34.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.4.0-b34
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.4.0-b34/hk2-locator-2.4.0-b34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.5.0
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.5.0/hk2-locator-2.5.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.5.0
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.5.0/hk2-locator-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-parent/2.4.0-b34
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-parent/2.4.0-b34/hk2-parent-2.4.0-b34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-parent/2.5.0
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-parent/2.5.0/hk2-parent-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.4.0-b34
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.4.0-b34/hk2-utils-2.4.0-b34.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.4.0-b34
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.4.0-b34/hk2-utils-2.4.0-b34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.5.0
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.5.0/hk2-utils-2.5.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.5.0
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.5.0/hk2-utils-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/pom/8
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/pom/8/pom-8.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/glassfish/hk2/external/2.4.0-b34/external-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/external/2.5.0/external-2.5.0.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.4.0-b34/aopalliance-repackaged-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.5.0/aopalliance-repackaged-2.5.0.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/external/aopalliance-repackaged/2.5.0/aopalliance-repackaged-2.5.0.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/external/jakarta.inject/2.5.0/jakarta.inject-2.5.0.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/external/jakarta.inject/2.5.0/jakarta.inject-2.5.0.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/external/javax.inject/2.4.0-b34/javax.inject-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.4.0-b34/hk2-api-2.4.0-b34.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.4.0-b34/hk2-api-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.5.0/hk2-api-2.5.0.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-api/2.5.0/hk2-api-2.5.0.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-bom/2.4.0-b34/hk2-bom-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-bom/2.5.0/hk2-bom-2.5.0.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.4.0-b34/hk2-locator-2.4.0-b34.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.4.0-b34/hk2-locator-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.5.0/hk2-locator-2.5.0.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-locator/2.5.0/hk2-locator-2.5.0.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-parent/2.4.0-b34/hk2-parent-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-parent/2.5.0/hk2-parent-2.5.0.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.4.0-b34/hk2-utils-2.4.0-b34.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.4.0-b34/hk2-utils-2.4.0-b34.pom
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.5.0/hk2-utils-2.5.0.jar
/usr/share/java/.m2/repository/org/glassfish/hk2/hk2-utils/2.5.0/hk2-utils-2.5.0.pom
/usr/share/java/.m2/repository/org/glassfish/pom/8/pom-8.pom
