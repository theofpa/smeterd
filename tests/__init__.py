class SerialMock(object):
    lines_in_buffer = []

    def __init__(self, port, *args, **kwargs):
        self.name = port
        self.open()

    def open(self):
        self.is_open = True;

    def close(self):
        self.is_open = False;

    def isOpen(self):
        return self.is_open

    def setRTS(self, value):
        pass

    def readline(self):
        if len(self.lines_in_buffer) > 0:
            return self.lines_in_buffer.pop(0)
        else:
            raise Exception('empty buffer')
            return ''



NORMAL_PACKET = '''/ISk5\2ME382-1004

0-0:96.1.1(4B414C37303035313135383130323132)
1-0:1.8.1(00608.400*kWh)
1-0:1.8.2(00490.342*kWh)
1-0:2.8.1(00000.001*kWh)
1-0:2.8.2(00000.000*kWh)
0-0:96.14.0(0001)
1-0:1.7.0(0001.51*kW)
1-0:2.7.0(0000.00*kW)
0-0:17.0.0(0999.00*kW)
0-0:96.3.10(1)
0-0:96.13.1()
0-0:96.13.0()
0-1:24.1.0(3)
0-1:96.1.0(3238303131303031323332313337343132)
0-1:24.3.0(130810180000)(00)(60)(1)(0-1:24.2.1)(m3)
(00947.680)
0-1:24.4.0(1)
!'''

BROKEN_PACKET = '''1-0:1.7.0(0001.51*kW)
1-0:2.7.0(0000.00*kW)
0-0:17.0.0(0999.00*kW)
0-0:96.3.10(1)
0-0:96.13.1()
0-0:96.13.0()
0-1:24.1.0(3)
0-1:96.1.0(3238303131303031323332313337343132)
0-1:24.3.0(130810180000)(00)(60)(1)(0-1:24.2.1)(m3)
(00947.680)
0-1:24.4.0(1)
!'''
