## 📖 Bachelor thesis: Raspberry-controlled sensors for smart user trial environments (2016)

Humans can easily be distracted by environmental conditions like temperature or brightness. Therefore user testing can be influenced by different room conditions. A former project focused on designing and implementing a user testing platform will therefore be extended by a display of the current room conditions in order to make stable user testing easier.  
  
The aim of this work is to build an inexpansive device capable of gathering data about the room conditions, storing and displaying the gathered data cloudless on a different local device, just using a Raspberry Pi 2 Model B and a self-assembled breadboard with sensors. The breadboard woll be controlled by a Python script running on the Raspberry device and will furthermore send data to a Ruby on Rails server running in the same network. The Rails platform did already exist and was extended for this work with the abilities to receive, display and save the data locally.

### 📎 Old instructions for the users it was implemented for:

`Es ist möglich, dass das Raspberry Pi erneut für das Eduroamnetzwerk konfiguriert werden muss,
da das Verbinden mit einem anderen Netzwerk womöglich die Config-File zerstört hat.
Sollte sich das Raspberry also wirklich nicht automatisch mit dem Eduroam verbinden,
nachdem es im Lab aufgestellt wurde, muss die Datei /etc/wpa_supplicant/wpa_supplicant.config verändert werden.
Der Eintrag mit dem es bereits funktionierte sollte noch erhalten sein,
jedoch sollte auch ein Weiterer vorliegen, der die Verbindung möglicherweise stört.
Ich empfehle den zweiten Eintrag zu löschen und zu rebooten.
Sollte dies nicht ausreichen, sieht man unter http://zid.univie.ac.at/support/anleitungen/netze-zugang/wlan-eduroam/linux-wicd/ wie dieser Eintrag auszusehen hat.`
