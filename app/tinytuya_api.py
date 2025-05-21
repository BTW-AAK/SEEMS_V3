import tinytuya

def get_device_status(device_id, ip, key):
    plug = tinytuya.OutletDevice(device_id, ip, key)
    plug.set_version(3.3)
    data = plug.status()
    dps = data.get('dps', {})
    return {
        'energy_wh': dps.get('22', 0.0),
        'voltage': dps.get('20', 0.0) / 10.0,
        'current': dps.get('18', 0.0) / 1000.0
    }

def set_device_power(device_id, ip, key, state: bool):
    plug = tinytuya.OutletDevice(device_id, ip, key)
    plug.set_version(3.3)
    plug.set_status(state, 1)
    return True
