import wmi

c = wmi.WMI()
listOfAllProcess = ['armsvc.exe', 'smss.exe', 'System', 'conhost.exe', 'DbxSvc.exe', 'LockApp.exe', 'WmiPrvSE.exe',
                    'browser_broker.exe', 'SearchProtocolHost.exe',
                    'RuntimeBroker.exe', 'MicrosoftEdgeSH.exe', 'ReflectMonitor.exe', 'SearchUI.exe', 'fontdrvhost.exe',
                    'fsnotifier64.exe', 'MicrosoftEdgeCP.exe',
                    'System Idle Process', 'SystemSettingsBroker.exe', 'pycharm64.exe', 'Microsoft.Photos.exe',
                    'SearchIndexer.exe', 'flux.exe', 'Memory Compression',
                    'NvTelemetryContainer.exe', 'RemindersServer.exe', 'SystemSettings.exe', 'spoolsv.exe',
                    'services.exe', 'SettingSyncHost.exe', 'SgrmBroker.exe',
                    'sihost.exe', 'ApplicationFrameHost.exe', 'TiltWheelMouse.exe', 'NVIDIA Share.exe',
                    'nvcontainer.exe', 'GWIdlMon.exe', 'MacriumService.exe',
                    'SecurityHealthService.exe', 'dasHost.exe', 'lsass.exe', 'winlogon.exe', 'ctfmon.exe',
                    'XtuService.exe', 'NVDisplay.Container.exe', 'svchost.exe',
                    'dllhost.exe', 'ReflectUI.exe', 'backgroundTaskHost.exe', 'Taskmgr.exe', 'WUDFHost.exe',
                    'Service_KMS.exe', 'WinStore.App.exe', 'AGSService.exe',
                    'AGMService.exe', 'pia-service.exe', 'ICCProxy.exe', 'csrss.exe', 'SearchFilterHost.exe',
                    'WindowsInternal.ComposableShell.Experiences.TextInput.InputApp.exe',
                    'nvsphelper64.exe', 'DropboxUpdate.exe', 'rundll32.exe', 'WPSHWPBC.exe', 'NVIDIA Web Helper.exe',
                    'OfficeClickToRun.exe', 'GWCtlSrv.exe', 'Registry', 'explorer.exe',
                    'python.exe', 'PnkBstrA.exe', 'dwm.exe', 'taskhostw.exe', 'MicrosoftEdge.exe',
                    'ShellExperienceHost.exe', 'chrome.exe', 'wininit.exe']


# listOfAllProcess= list(set(listOfAllProcess))

class BST(object):
    class Node(object):
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = self.Node()

    def put(self, value):
        self._put(value, self.root)

    def _put(self, value, node):
        if node.value is None:
            node.value = value
        else:
            if value < node.value:
                if node.left is None:
                    node.left = self.Node()
                self._put(value, node.left)
            else:
                if node.right is None:
                    node.right = self.Node()
                self._put(value, node.right)

    def contains(self, value):
        return self._contains(value, self.root)

    def _contains(self, value, node):
        if node is None or node.value is None:
            return False
        else:
            if value == node.value:
                return True
            elif value < node.value:
                return self._contains(value, node.left)
            else:
                return self._contains(value, node.right)

    def in_order_traversal(self):
        acc = list()
        self._in_order_traversal(self.root, acc)
        return acc

    def _in_order_traversal(self, node, acc):
        if node is None or node.value is None:
            return
        self._in_order_traversal(node.left, acc)
        acc.append(node.value)
        self._in_order_traversal(node.right, acc)


tree = BST()
# print(tree.in_order_traversal())


setOfRunning = set()

for process in c.Win32_Process():
    if process.name == 'Taskmgr.exe':
        print("!!!")
    # print(process.ProcessId, process.Name)
    # tree.put(process.Name)
    setOfRunning.add(process.Name)

notWhitelisted = setOfRunning.difference(listOfAllProcess)
print("notWhitelisted:")
print(notWhitelisted)

print("expected, but not present:")
print(set(listOfAllProcess).difference(setOfRunning))

### above is for task master
### below is
