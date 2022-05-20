import time

def _run_backtest(self):
    while True:
        if self.data_handler.continue_backtest == True:
            self.data_handler.update_bars()  # Trigger a market event
        else:
            break
        while True:
            try:
                event = self.events.get(False)  ##Get an event from the Queue
            except queue.Empty:
                break
            else:
                if event is not None:
                    if event.type == 'MARKET':
                        self.strategy.calculate_signals(event)  
                        ## Trigger a Signal event #
                        self.portfolio.update_timeindex()
                    elif event.type == 'SIGNAL':
                        self.signals += 1
                        self.portfolio.update_signal(event)  
                        # Transfer Signal Event to order Event and trigger an order event
                    elif event.type == 'ORDER':
                        self.orders += 1
                        self.execution_handler.execute_order(event)
                    elif event.type == 'FILL':
                        self.fills += 1
                        self.portfolio.update_fill(event)
            time.sleep(self.heartbeat)
