import datetime
import trio

class MonopolyGateway:
    ''' Main Monopoly API Gateway class
    '''

    def __init__(self, confParser):
        pass


    async def create_nursery(self, port):
        ''' Create trio nursery '''
        async with trio.open_nursery(self) as nursery:
            nursery.start_soon(trio.serve_tcp, self.handler, port)



    def run(self):
        ''' Run connaction handle '''
        try:
            trio.run(self.create_nursery, 1682)
        except KeyboardInterrupt as e:
            print(str(e))


    async def handler(self, connStream):
        ''' Handler for incoming connection '''
        while True:
            data = await connStream.receive_some(2048)
            if data:
                print('Received\t {}'.format(data))
                await connStream.send_all(data)
            else:
                break
