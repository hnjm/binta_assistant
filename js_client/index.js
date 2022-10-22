var host = 'ws://localhost:2700'

webSocket = new WebSocket(host);

// ** receiving message
webSocket.onmessage = (event) => {
    console.log(event.data);
  }


// ** 