def return_query_for_host(address, port):
    if port:
        if int(port) is 161:
            return {"address": address}
        return {"address": address, "port": port}
    else:
        return {"address": address}


def return_task_name(address, port):
    if port:
        if int(port) is 161:
            return address
        return f"{address}:{port}"
    else:
        return address
