#!/usr/bin/python2.7
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        h1 = self.addHost( 'h1' )
        s1 = self.addSwitch( 's1', listenPort=6635 )
        h2 = self.addHost( 'h2' )
        s2 = self.addSwitch( 's2', listenPort=6636 )
        h4 = self.addHost( 'h4' )
        s4 = self.addSwitch( 's4', listenPort=6638 )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        s3 = self.addSwitch( 's3', listenPort=6637 )

        # Adding links between hosts and switches
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h4, s4 )

        self.addLink( h5, s3 )
        self.addLink( h6, s3 )
        self.addLink( h7, s3 )
        self.addLink( h8, s3 )


        self.addLink( s1, s2)
        self.addLink( s1, s4)
        self.addLink( s2, s3)



def starter():
        topology = MyTopo()
        net = Mininet(topo=topology, controller=None)

        h1 = net.get( 'h1' )
        h1.intf( 'h1-eth0' ).setIP( '10.0.1.2', 24 )
        h1.intf( 'h1-eth0' ).setMAC( '0A:00:01:02:00:00' )
        h2 = net.get( 'h2' )
        h2.intf( 'h2-eth0' ).setIP( '10.0.2.2', 24 )
        h2.intf( 'h2-eth0' ).setMAC( '0A:00:02:02:00:00' )

        h4 = net.get( 'h4' )
        h4.intf( 'h4-eth0' ).setIP( '10.0.4.2', 24 )
        h4.intf( 'h4-eth0' ).setMAC( '0A:00:04:02:00:00' )
        h5 = net.get( 'h5' )
        h5.intf( 'h5-eth0' ).setIP( '10.0.5.2', 24 )
        h5.intf( 'h5-eth0' ).setMAC( '0A:00:05:02:00:00' )
        h6 = net.get( 'h6' )
        h6.intf( 'h6-eth0' ).setIP( '10.0.6.2', 24 )
        h6.intf( 'h6-eth0' ).setMAC( '0A:00:06:02:00:00' )
        h7 = net.get( 'h7' )
        h7.intf( 'h7-eth0' ).setIP( '10.0.7.2', 24 )
        h7.intf( 'h7-eth0' ).setMAC( '0A:00:07:02:00:00' )
        h8 = net.get( 'h8' )
        h8.intf( 'h8-eth0' ).setIP( '10.0.8.2', 24 )
        h8.intf( 'h8-eth0' ).setMAC( '0A:00:08:02:00:00' )

        
        net.start()
        dumpNodeConnections(net.hosts)
        CLI(net)
        net.stop()

setLogLevel('info')
starter()
