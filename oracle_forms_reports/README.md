#HOWTO Install Oracle Forms/Reports 12.2.1.3 on Windows 7 SP1#
Environment:  
VirtualBox machine 4Gb Memory  
OS Windows 7 SP1 Professional 64bit  

##1.Check system requirements
Link: https://www.oracle.com/technetwork/middleware/fmw-122130-certmatrix-3867828.xlsx  
##2.Download software  
###2.1.Oracle JDK 1.8.0_131
Link: https://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html  
![1.Download Oracle JDK](images/img1_jdk_download.jpg)  
2.2.Microsoft Visual C++ https://www.microsoft.com/en-us/download/details.aspx?id=30679  
![2.Download Microsoft Visual C++](images/img2_ms_visual_cpp_download.jpg)  
2.3.ADF(Application Development Framework) Infrastructure 12.2.1.3, https://www.oracle.com/technetwork/developer-tools/adf/downloads/index.html  
![3.Download ADF Infrastructure](images/img3_adf_infrastructure_download.jpg)  
2.4.Oracle Forms https://www.oracle.com/downloads/,  “Developer Downloads” chapter > “Middleware” chapter > "Forms and Reports Services" link  
![4.Forms Download](images/img4_forms_download.jpg)  
<p align="center">Pic 3: Oracle Forms Download</p>  


![5.Forms Download,edelivery](images/img5_forms_download.jpg)  
<p align="center">Pic 5: Oracle Forms Download, edelivery.oracle.com</p>  


![6.License Agreement](images/img6_forms_download.jpg)  
<p align="center">Pic 6: License Agreement</p>  


![7.Forms Download,edelivery,zip files](images/img7_forms_download.jpg)  
<p align="center">Pic 7: Forms Download, zip files, edelivery.oracle.com</p>  


Unzip both zip files into thee same folder  


3.Install Oracle JDK to the folder with the "8.3" name  
"8.3" name means following: https://en.wikipedia.org/wiki/8.3_filename  
![8.JDK folder name](images/img8_jdk_installation_folder_name.jpg)  
<p align="center">Pic 8: JDK folder name</p>  


![9.JRE folder name](images/img9_jdk_installation_jre_folder_name.jpg)  
<p align="center">Pic 9: JRE folder name</p>  


4.Install Microsoft Visual C++  
Restart computer after installation of Microsoft Visual C++  

5.Install Application Development Framework Infrastructure  

6.Install ADF Infrastructure   
Run cmd as Administrator  
Change directory to the folder with unpacked ADF Infrastructure distro  
Run ADF Infrastructure Installer. Example:  
```
e:\app\java\jdk1.8.0_131\bin\java.exe -jar fmw_12.2.1.3.0_infrastructure.jar
```
![10.ADF Infrastructure Installation. Select Oracle Home folder](images/img10_adf_infra_installation.jpg)  
<p align="center">Pic 10: ADF Infrastructure Installation. Select Oracle Home folder</p>  


7.Install Oracle Forms 12.2.1.3  
run setup_fmw_12.2.1.3.0_fr_win64.exe as Administrator  
![11.Forms Installation. Select ADF Infrastructure Oracle Home](images/img11_forms_installation_select_adf_infrastructure_oracle_home.jpg)  
<p align="center">Pic 11: Forms Installation. Select ADF Infrastructure Oracle Home</p>  


References:  
Documentation: https://docs.oracle.com/middleware/12213/formsandreports/index.html  
System requirements: https://www.oracle.com/technetwork/middleware/fmw-122130-certmatrix-3867828.xlsx  
Download Oracle JDK 1.8.0_131: https://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html  
Download Application Development Runtime 12.2.1.3: https://www.oracle.com/technetwork/developer-tools/adf/downloads/index.html  
Download Microsoft Visual C++: https://www.microsoft.com/en-us/download/details.aspx?id=30679  




