1. First fix IP of the laptop
![fix-local-ip](https://github.com/davizuku/marc_on_da_house/raw/master/doc/fix-local-ip.png)
1. Choose a port, e.g. 98765
2. Get your public IP from: https://www.hashemian.com/whoami/
3. Configure your router to redirect <public-ip>:<port> -> <local-ip>:<port>
   1. https://www.lowi.es/asistencia/como-abro-un-puerto-o-todos-los-puertos-del-router/
   2. ![port-redirect](https://github.com/davizuku/marc_on_da_house/raw/master/doc/port-redirect.png)
4. Change the port used by `api/index.js` to start the API service
5. Start the service
