from celery import Celery,shared_task, Task

import compile_lang
import pb_compiler_pb2
from compile_lang_enums import SUPPORTED_LANGUAGES
from threading import Thread

app = Celery('tasks', backend='amqp', broker='amqp://localhost//')
# producer = compile_lang.CompilerProducer()

class ProducerTask(Task):
    abstract = True
    _cp = None

    @property
    def producer(self):
        print('accessing producer')
        if ProducerTask._cp is None:
            print('instantiating producer')
            ProducerTask._cp = compile_lang.CompilerProducer()
            self.producer_thread = Thread(target=self._cp)
            self.producer_thread.start()
        print('returning producer')
        return ProducerTask._cp

@shared_task
def test(msg):
    print(msg)
    return msg

@shared_task(base=ProducerTask)
def fwd_req(lang, code):
    """
    returns None if compiler is unavailable
    """
    print('forwarding request lang {}'.format(lang))
    if fwd_req.producer.dispatch_req(lang, code) == -1:
        return None
    res = fwd_req.producer.get_compile_result()
    return res

@shared_task(base=ProducerTask)
def start():
    start.producer
    return 0 
