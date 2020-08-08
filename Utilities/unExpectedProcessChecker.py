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

setOfRunning = set()

for process in c.Win32_Process():
    if process.name == 'Taskmgr.exe':
        print("!!! Taskmgr.exe")
    # print(process.ProcessId, process.Name)
    setOfRunning.add(process.Name)

notWhitelisted = setOfRunning.difference(listOfAllProcess)
print(f"notWhitelisted: {notWhitelisted}")

diff = set(listOfAllProcess).difference(setOfRunning)
print(f"expected, but not present: {diff}")
