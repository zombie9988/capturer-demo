import asyncio
import grp
import logging
from math import log

import grpc

from alert_pb2 import *
from alert_pb2_grpc import *

send_alert_message = Alert()
send_alert_message.d_ip = "192.168.1.1"
send_alert_message.src_ip = "192.168.1.1"
send_alert_message.rule_type = Alert.RULE_NOTE
send_alert_message.date = "11.05.2022"

class Capturer(AlertCapturer):
    async def SendAlert(
        self,
        request: Alert,
        context: grpc.aio.ServicerContext,
        ) -> Result:
            await self.Write(request=request)
            return Result(res_type=Result.RES_OK)
        
    async def Write(self, request: Alert):
        logging.info(f"Alert: {request.rule_type} from {request.src_ip} to {request.d_ip}")

async def serve():
    server = grpc.aio.server()
    add_AlertCapturerServicer_to_server(Capturer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    logging.info("Server start listening")
    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())