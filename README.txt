Es ist m�glich, dass das Raspberry Pi erneut f�r das Eduroamnetzwerk konfiguriert werden muss,
da das Verbinden mit einem anderen Netzwerk wom�glich die Config-File zerst�rt hat.
Sollte sich das Raspberry also wirklich nicht automatisch mit dem Eduroam verbinden,
nachdem es im Lab aufgestellt wurde, muss die Datei /etc/wpa_supplicant/wpa_supplicant.config ver�ndert werden.
Der Eintrag mit dem es bereits funktionierte sollte noch erhalten sein,
jedoch sollte auch ein Weiterer vorliegen, der die Verbindung m�glicherweise st�rt.
Ich empfehle den zweiten Eintrag zu l�schen und zu rebooten.
Sollte dies nicht ausreichen, sieht man unter

http://zid.univie.ac.at/support/anleitungen/netze-zugang/wlan-eduroam/linux-wicd/

wie dieser Eintrag auszusehen hat.
