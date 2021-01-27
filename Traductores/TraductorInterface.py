class TraductorInterface:
    isRunning = False
    colaImpresion = []

    def __init__(self, comando, *args):
        self.comando = comando

    def run(self, jsonTicket):
        actions = jsonTicket.keys()
        rta = []
        for action in actions:
            if action == "listcommand":
                actionlist = jsonTicket[action]
                for action1 in actionlist:
                    lista2 = action1
                    for action2 in lista2:
                        try:
                            fnAction1 = getattr(self, action2)
                            if isinstance(lista2[action2], list):
                                res1 = fnAction1(*lista2[action2])
                                rta.append({"action": action2, "params":lista2[action2],"rta": res1})
                            elif isinstance(lista2[action2], dict):
                                res1 = fnAction1(**lista2[action2])
                                rta.append({"action": action2,"params":lista2[action2], "rta": res1})
                            else:
                                res1 = fnAction1(lista2[action2])
                                rta.append({"action": action2, "params":lista2[action2], "rta": res1})   
                        except Exception as e:
                            reserror = str(e)
                            rta.append({"action": action2, "params":lista2[action2], "err": reserror})
            else:
                try:
                    fnAction = getattr(self, action)
                    if isinstance(jsonTicket[action], list):
                        res = fnAction(*jsonTicket[action])
                        rta.append({"action": action, "params":jsonTicket[action], "rta": res})

                    elif isinstance(jsonTicket[action], dict):
                        res = fnAction(**jsonTicket[action])
                        rta.append({"action": action, "params":jsonTicket[action], "rta": res})
                    else:
                        res = fnAction(jsonTicket[action])
                except Exception as e:
                    reserror = str(e)
                    rta.append({"action": action, "params":jsonTicket[action], "err": reserror})
        return rta
