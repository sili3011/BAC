Es ist möglich, dass das Raspberry Pi erneut für das Eduroamnetzwerk konfiguriert werden muss,
da das Verbinden mit einem anderen Netzwerk womöglich die Config-File zerstört hat.
Sollte sich das Raspberry also wirklich nicht automatisch mit dem Eduroam verbinden,
nachdem es im Lab aufgestellt wurde, muss die Datei /etc/wpa_supplicant/wpa_supplicant.config verändert werden.
Der Eintrag mit dem es bereits funktionierte sollte noch erhalten sein,
jedoch sollte auch ein Weiterer vorliegen, der die Verbindung möglicherweise stört.
Ich empfehle den zweiten Eintrag zu löschen und zu rebooten.
Sollte dies nicht ausreichen, sieht man unter

http://zid.univie.ac.at/support/anleitungen/netze-zugang/wlan-eduroam/linux-wicd/

wie dieser Eintrag auszusehen hat.
