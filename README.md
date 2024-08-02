# TCP client

This code example demonstrates the implementation of a TCP client with PSoC&trade; 6 MCU with AIROC&trade; CYW43xxx Wi-Fi & Bluetooth&reg; combo chips. This example establishes a connection with a remote TCP server based on the command received from the TCP server, which turns the user LED ON or OFF. Additionally, this code example can be configured to bring up the Wi-Fi device either in STA interface or Soft AP interface mode.

This example uses the Wi-Fi Core FreeRTOS lwIP mbedtls library of the SDK. This library enables application development based on Wi-Fi by pulling wifi-connection-manager, FreeRTOS, lwIP, mbed TLS, secure sockets, and other dependent modules. The secure sockets library provides an easy-to-use API by abstracting the network stack (lwIP) and the security stack (mbed TLS).

This example can be modified to use ThreadX and NetX Duo instead of FreeRTOS and lwIP. See the [Design and implementation](#design-and-implementation) section for more details.

[View this README on GitHub.](https://github.com/Infineon/mtb-example-wifi-tcp-client)

[Provide feedback on this code example.](https://cypress.co1.qualtrics.com/jfe/form/SV_1NTns53sK2yiljn?Q_EED=eyJVbmlxdWUgRG9jIElkIjoiQ0UyMjkxMTIiLCJTcGVjIE51bWJlciI6IjAwMi0yOTExMiIsIkRvYyBUaXRsZSI6IlRDUCBjbGllbnQiLCJyaWQiOiJwYXRoaXN1ZGhhcnMiLCJEb2MgdmVyc2lvbiI6IjQuMi4wIiwiRG9jIExhbmd1YWdlIjoiRW5nbGlzaCIsIkRvYyBEaXZpc2lvbiI6Ik1DRCIsIkRvYyBCVSI6IklDVyIsIkRvYyBGYW1pbHkiOiJQU09DIn0=)


## Requirements

- [ModusToolbox&trade;](https://www.infineon.com/modustoolbox) v3.1 or later (tested with v3.1)
- Board support package (BSP) minimum required version: 4.0.0
- Programming language: C
- Associated parts: All [PSoC&trade; 6 MCU](https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-6-32-bit-arm-cortex-m4-mcu) parts, [AIROC&trade; CYW20819 Bluetooth&reg; & Bluetooth&reg; LE SoC](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-bluetooth-le-bluetooth-multiprotocol/airoc-bluetooth-le-bluetooth/cyw20819), [AIROC&trade; CYW43012 Wi-Fi & Bluetooth&reg; combo chip](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43012), [AIROC&trade; CYW4343W Wi-Fi & Bluetooth&reg; combo chip](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw4343w), [AIROC&trade; CYW4373 Wi-Fi & Bluetooth&reg; combo chip](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-5-802.11ac/cyw4373), [AIROC&trade; CYW43439 Wi-Fi & Bluetooth&reg; combo chip](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43439),[AIROC&trade; CYW43022 Wi-Fi & Bluetooth&reg; combo chip](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-5-802.11ac/cyw43022)

## Supported toolchains (make variable 'TOOLCHAIN')

- GNU Arm&reg; Embedded Compiler v11.3.1 (`GCC_ARM`) – Default value of `TOOLCHAIN`
- Arm&reg; Compiler v6.16 (`ARM`)
- IAR C/C++ Compiler v9.30.1 (`IAR`)

## Supported kits (make variable 'TARGET')

- [PSoC&trade; 6 Wi-Fi Bluetooth&reg; Prototyping Kit](https://www.infineon.com/CY8CPROTO-062-4343W) (`CY8CPROTO-062-4343W`) – Default value of `TARGET`
- [PSoC&trade; 6 Wi-Fi Bluetooth&reg; Pioneer Kit](https://www.infineon.com/CY8CKIT-062-WIFI-BT) (`CY8CKIT-062-WIFI-BT`)
- [PSoC&trade; 62S2 Wi-Fi Bluetooth&reg; Pioneer Kit](https://www.infineon.com/CY8CKIT-062S2-43012) (`CY8CKIT-062S2-43012`)
- [PSoC&trade; 62S1 Wi-Fi Bluetooth&reg; Pioneer Kit](https://www.infineon.com/CYW9P62S1-43438EVB-01) (`CYW9P62S1-43438EVB-01`)
- [PSoC&trade; 62S1 Wi-Fi Bluetooth&reg; Pioneer Kit](https://www.infineon.com/CYW9P62S1-43012EVB-01) (`CYW9P62S1-43012EVB-01`)
- [PSoC&trade; 62S3 Wi-Fi Bluetooth&reg; Prototyping Kit](https://www.infineon.com/CY8CPROTO-062S3-4343W) (`CY8CPROTO-062S3-4343W`)
- [PSoC&trade; 64 "Secure Boot" Wi-Fi Bluetooth&reg; Pioneer Kit](https://www.infineon.com/CY8CKIT-064B0S2-4343W) (`CY8CKIT-064B0S2-4343W`)
- [PSoC&trade; 62S2 Evaluation Kit](https://www.infineon.com/CY8CEVAL-062S2) (`CY8CEVAL-062S2-LAI-4373M2`, `CY8CEVAL-062S2-MUR-43439M2`,`CY8CEVAL-062S2-CYW43022CUB` , `CY8CEVAL-062S2-CYW955513SDM2WLIPA`)

## Hardware setup

This example uses the board's default configuration. See the kit user guide to ensure that the board is configured correctly.

**Note:** The PSoC&trade; 6 Wi-Fi Bluetooth&reg; Pioneer Kit (CY8CKIT-062-WIFI-BT) ships with KitProg2 installed. The ModusToolbox&trade; software requires KitProg3. Before using this code example, make sure that the board is upgraded to KitProg3. The tool and instructions are available in the [Firmware Loader](https://github.com/Infineon/Firmware-loader) GitHub repository. If you do not upgrade, you will see an error like "unable to find CMSIS-DAP device" or "KitProg firmware is out of date".


## Software setup

1. Install a terminal emulator if you don't have one. Instructions in this document use [Tera Term](https://teratermproject.github.io/index-en.html).

2. Install a Python interpreter if you don't have one. This code example is tested using [Python 3.7.7](https://www.python.org/downloads/release/python-377/).

## Using the code example

### Create the project

The ModusToolbox&trade; tools package provides the Project Creator as both a GUI tool and a command line tool.

<details><summary><b>Use Project Creator GUI</b></summary>

1. Open the Project Creator GUI tool.

   There are several ways to do this, including launching it from the dashboard or from inside the Eclipse IDE. For more details, see the [Project Creator user guide](https://www.infineon.com/ModusToolboxProjectCreator) (locally available at *{ModusToolbox&trade; install directory}/tools_{version}/project-creator/docs/project-creator.pdf*).

2. On the **Choose Board Support Package (BSP)** page, select a kit supported by this code example. See [Supported kits](#supported-kits-make-variable-target).

   > **Note:** To use this code example for a kit not listed here, you may need to update the source files. If the kit does not have the required resources, the application may not work.

3. On the **Select Application** page:

   a. Select the **Applications(s) Root Path** and the **Target IDE**.

   > **Note:** Depending on how you open the Project Creator tool, these fields may be pre-selected for you.

   b.	Select this code example from the list by enabling its check box.

   > **Note:** You can narrow the list of displayed examples by typing in the filter box.

   c. (Optional) Change the suggested **New Application Name** and **New BSP Name**.

   d. Click **Create** to complete the application creation process.

</details>

<details><summary><b>Use Project Creator CLI</b></summary>

The 'project-creator-cli' tool can be used to create applications from a CLI terminal or from within batch files or shell scripts. This tool is available in the *{ModusToolbox&trade; install directory}/tools_{version}/project-creator/* directory.

Use a CLI terminal to invoke the 'project-creator-cli' tool. On Windows, use the command-line 'modus-shell' program provided in the ModusToolbox&trade; installation instead of a standard Windows command-line application. This shell provides access to all ModusToolbox&trade; tools. You can access it by typing "modus-shell" in the search box in the Windows menu. In Linux and macOS, you can use any terminal application.

The following example clones the "[mtb-example-wifi-tcp-client](https://github.com/Infineon/mtb-example-wifi-tcp-client)" application with the desired name "TcpClient" configured for the *CY8CPROTO-062S2-43439* BSP into the specified working directory, *C:/mtb_projects*:

   ```
   project-creator-cli --board-id CY8CPROTO-062S2-43439 --app-id mtb-example-wifi-tcp-client --user-app-name TcpClient --target-dir "C:/mtb_projects"
   ```

The 'project-creator-cli' tool has the following arguments:

Argument | Description | Required/optional
---------|-------------|-----------
`--board-id` | Defined in the <id> field of the [BSP](https://github.com/Infineon?q=bsp-manifest&type=&language=&sort=) manifest | Required
`--app-id`   | Defined in the <id> field of the [CE](https://github.com/Infineon?q=ce-manifest&type=&language=&sort=) manifest | Required
`--target-dir`| Specify the directory in which the application is to be created if you prefer not to use the default current working directory | Optional
`--user-app-name`| Specify the name of the application if you prefer to have a name other than the example's default name | Optional

> **Note:** The project-creator-cli tool uses the `git clone` and `make getlibs` commands to fetch the repository and import the required libraries. For details, see the "Project creator tools" section of the [ModusToolbox&trade; tools package user guide](https://www.infineon.com/ModusToolboxUserGuide) (locally available at {ModusToolbox&trade; install directory}/docs_{version}/mtb_user_guide.pdf).

</details>

### Open the project

After the project has been created, you can open it in your preferred development environment.

<details><summary><b>Eclipse IDE</b></summary>

If you opened the Project Creator tool from the included Eclipse IDE, the project will open in Eclipse automatically.

For more details, see the [Eclipse IDE for ModusToolbox&trade; user guide](https://www.infineon.com/MTBEclipseIDEUserGuide) (locally available at *{ModusToolbox&trade; install directory}/docs_{version}/mt_ide_user_guide.pdf*).

</details>


<details><summary><b>Visual Studio (VS) Code</b></summary>

Launch VS Code manually, and then open the generated *{project-name}.code-workspace* file located in the project directory.

For more details, see the [Visual Studio Code for ModusToolbox&trade; user guide](https://www.infineon.com/MTBVSCodeUserGuide) (locally available at *{ModusToolbox&trade; install directory}/docs_{version}/mt_vscode_user_guide.pdf*).

</details>


<details><summary><b>Keil µVision</b></summary>

Double-click the generated *{project-name}.cprj* file to launch the Keil µVision IDE.

For more details, see the [Keil µVision for ModusToolbox&trade; user guide](https://www.infineon.com/MTBuVisionUserGuide) (locally available at *{ModusToolbox&trade; install directory}/docs_{version}/mt_uvision_user_guide.pdf*).

</details>


<details><summary><b>IAR Embedded Workbench</b></summary>

Open IAR Embedded Workbench manually, and create a new project. Then select the generated *{project-name}.ipcf* file located in the project directory.

For more details, see the [IAR Embedded Workbench for ModusToolbox&trade; user guide](https://www.infineon.com/MTBIARUserGuide) (locally available at *{ModusToolbox&trade; install directory}/docs_{version}/mt_iar_user_guide.pdf*).

</details>


<details><summary><b>Command line</b></summary>

If you prefer to use the CLI, open the appropriate terminal, and navigate to the project directory. On Windows, use the command-line 'modus-shell' program; on Linux and macOS, you can use any terminal application. From there, you can run various `make` commands.

For more details, see the [ModusToolbox&trade; tools package user guide](https://www.infineon.com/ModusToolboxUserGuide) (locally available at *{ModusToolbox&trade; install directory}/docs_{version}/mtb_user_guide.pdf*).

</details>

## Operation

If using a PSoC&trade; 64 "Secure" MCU kit (like CY8CKIT-064B0S2-4343W), the PSoC&trade; 64 device must be provisioned with keys and policies before being programmed. Follow the instructions in the ["Secure Boot" SDK user guide](https://www.infineon.com/dgdlac/Infineon-PSoC_64_Secure_MCU_Secure_Boot_SDK_User_Guide-Software-v07_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f8c361a7666) to provision the device. If the kit is already provisioned, copy-paste the keys and policy folder to the application folder.

**Note:**  Use `policy_single_CM0_CM4_smif_swap.json` policy instead of using the default one "policy_single_CM0_CM4_swap.json" to provision CY8CKIT-064B0S2-4343W device.

1. Connect the board to your PC using the provided USB cable through the KitProg3 USB connector.

2. The kit can be configured to run either in the Wi-Fi STA or AP interface modes. Configure the interface mode using the `USE_AP_INTERFACE` macro defined in the *tcp_client.c* file. Based on the desired interface mode, do the following:

   **Kit in STA mode (default interface):**

   1. Set the `USE_AP_INTERFACE` macro to '0'; default mode.

   2. Modify the `WIFI_SSID`, `WIFI_PASSWORD`, and `WIFI_SECURITY_TYPE` macros to match the Wi-Fi network credentials that you want to connect to in the *tcp_client.c* file. Ensure to configure your connecting Wi-Fi network as a private network for the proper functioning of this example.

   **Kit in AP mode:**

   1. Set the `USE_AP_INTERFACE` macro to '1'.

   2. (Optional) Update the `SOFTAP_SSID`, `SOFTAP_PASSWORD`, and `SOFTAP_SECURITY_TYPE` as desired.

3. Open a terminal program and select the KitProg3 COM port. Set the serial port parameters to 8N1 and 115200 baud.

4. Program the board using one of the following:

   <details><summary><b>Using Eclipse IDE for ModusToolbox&trade; software</b></summary>

      1. Select the application project in the Project Explorer.

      2. In the **Quick Panel**, scroll down, and click **\<Application Name> Program (KitProg3_MiniProg4)**.
      </details>

   <details><summary><b>Using CLI</b></summary>

     From the terminal, execute the `make program` command to build and program the application using the default toolchain to the default target. The default toolchain is specified in the application's Makefile but you can override this value manually:
      ```
      make program TOOLCHAIN=<toolchain>
      ```

      Example:
      ```
      make program TOOLCHAIN=GCC_ARM
      ```
   </details>

   **Figure 1. Wi-Fi connectivity status in STA mode**

   ![](images/tcp-client-sta-pre-connection.png)

   <br />

   **Figure 2. Wi-Fi connectivity status in AP mode**

   ![](images/tcp-client-ap-pre-connection.png)


5. Connect your PC to the Wi-Fi AP that you have configured in **Step 2**.

   - In STA mode: Connect the PC to the same AP to which the kit is connected.

   - In AP mode: Connect the PC to the kit's AP.

6. Open a command shell from the project directory and run the Python TCP server (*tcp_server.py*). Enter the following command:

   ```
   python tcp_server.py
   ```

  Note the TCP server's IPv4 address.

   **Note:** Ensure that the firewall settings of your PC allow access to the Python software to communicate with the TCP client. For more details on enabling Python access, see the [community thread](https://community.infineon.com/thread/53662).

   **Figure 3. TCP server IPv4 address**

   ![](images/tcp-server-ip-address.png)


7. From the UART terminal, enter the IPv4 address for the TCP server as noted in **Step 6**.

   For example, if the TCP server IPv4 address is 192.168.10.2, then enter the IP address from the UART terminal as shown in **Figure 4** and press the **Enter** key.

   **Figure 4. Entering the IPv4 address from the UART terminal**

   ![](images/uart-terminal-ipv4-input.png)

8. From the Python TCP server, send the command to turn the LED ON or OFF to the TCP client ('0' and '1' to turn the LED OFF and ON respectively). Observe the user LED (CYBSP_USER_LED) turning ON/OFF on the board.

   **Figure 5. TCP server output**

   ![](images/tcp-server-output.png)

   <br />

   **Figure 6. LED status on TCP client STA mode**

   ![](images/tcp-client-sta-post-connection.png)

   <br />

   **Figure 6. LED status on TCP client AP mode**

   ![](images/tcp-client-ap-post-connection.png)


**Note:** Instead of using the Python TCP server (*tcp_server.py*), you can use the example [mtb-example-wifi-tcp-server](https://github.com/Infineon/mtb-example-wifi-tcp-server) to run as the TCP server on a second kit. See the code example documentation.


## Debugging

You can debug the example to step through the code. In the IDE, use the **\<Application Name> Debug (KitProg3_MiniProg4)** configuration in the **Quick Panel**. For details, see the "Program and debug" section in the [Eclipse IDE for ModusToolbox&trade; software user guide](https://www.infineon.com/MTBEclipseIDEUserGuide).

**Note:** **(Only while debugging)** On the CM4 CPU, some code in `main()` may execute before the debugger halts at the beginning of `main()`. This means that some code executes twice - once before the debugger stops execution, and again after the debugger resets the program counter to the beginning of `main()`. See [KBA231071](https://community.infineon.com/docs/DOC-21143) to learn about this and for the workaround.


## Design and implementation

### Resources and settings


**Table 1. Application resources**

 Resource  |  Alias/object     |    Purpose
 :------- | :------------    | :-----------
 SDIO (HAL) | sdio_obj | SDIO interface for Wi-Fi connectivity
 UART (HAL) |cy_retarget_io_uart_obj| UART HAL object used by Retarget-IO for the Debug UART port
 LED (BSP) | CYBSP_USER_LED | User LED to show the output

<br />

This example uses the Arm&reg; Cortex&reg;-M4 (CM4) CPU of PSoC&trade; 6 MCU to execute an RTOS task: TCP client task. At device reset, the default Cortex&reg;-M0+ (CM0+) application enables the CM4 CPU and configures the CM0+ CPU to go to sleep.

In this example, PSoC&trade; 6 MCU is configured as a TCP client, which establishes a connection with a remote TCP server, and based on the command received from the TCP server, turns the user LED (CYBSP_USER_LED) ON or OFF.

### Using ThreadX and NetX Duo

This code example can be modified to use the ThreadX and NetX Duo instead of the default FreeRTOS and lwIP. All the source and configuration files required by both the RTOSes are already present in their COMPONENT_* folders. By default, the FreeRTOS and lwIP libraries are added as dependencies in this code example. Follow these steps to configure the code example to use ThreadX and NetX Duo instead.

<details><summary><b>Adding ThreadX and NetX Duo libraries</b></summary>

   1. In the **Quick Panel**, scroll down, and click **Library Manger \<version>**.
   2. In the **Library Manager** window, delete the **wifi-core-freertos-lwip-mbedtls** library. This will delete all the dependent libraries as well.
   3. Click the **Add Library** button and add the following libraries back. This step requires a bundle repo for ThreadX, NetX Duo, and NetX Secure does not exist.
      ```
      abstraction-rtos
      clib-support
      connectivity-utilities
      netxduo-network-interface-integration
      secure-sockets
      whd-bsp-integration
      wifi-connection-manager
      wifi-host-driver
      ```
   4. Click **OK** and **Update**. After the libraries are updated, click **Close**.
   5. The ThreadX and NetX Duo libraries do not show up in the library manager as these are not distributed by Infineon. Add these libraries manually. To add the ThreadX library, create a file called *threadx.mtb* in the **deps** folder of the code example with the following content:
   ```
   https://github.com/azure-rtos/threadx#v6.1.5_rel#$$ASSET_REPO$$/threadx/v6.1.5_rel
   ```
   6. To add the NetX Duo library, create a file called *netxduo.mtb* in the **deps** folder with the following content:
   ```
   https://github.com/azure-rtos/netxduo#v6.2.0_rel#$$ASSET_REPO$$/netxduo/v6.2.0_rel
   ```
   7. From the Terminal window, execute the `make getlibs` command to fetch these libraries.

   </details>

<details><summary><b>Makefile changes</b></summary>

   1. Change the following lines from
   ```
   COMPONENTS=FREERTOS
   ```
   to
   ```
   COMPONENTS=THREADX
   ```
</details>

Follow the steps in the [Using the code example](#using-the-code-example) section to run this code example.

**Note:** NetXDuo network stack used with ThreadX does not have the option to dynamically configure the TCP keep alive parameters (interval, count, and idle time). Therefore, the secure sockets `cy_socket_setsockopt` function fails with an error code "CY_RSLT_MODULE_SECURE_SOCKETS_OPTION_NOT_SUPPORTED".

In the code example, you can skip `cy_socket_setsockopt` calls (except CY_SOCKET_SO_TCP_KEEPALIVE_ENABLE) related to TCP keepalive in the ThreadX environment. And you can configure the desired TCP keep alive parameters by changing the following defines in *nx_user.h* file:
```
NX_TCP_KEEPALIVE_RETRIES
NX_TCP_KEEPALIVE_INITIAL
NX_TCP_KEEPALIVE_RETRY
```

**Note:** The version of the code example currently supports ThreadX and the NetXDuo network stack in GCC_ARM toolchain only. Support for other toolchains will be added in a future version of the code example.

<br />

## Related resources

Resources  | Links
-----------|----------------------------------
Application notes  | [AN228571](https://www.infineon.com/AN228571) – Getting started with PSoC&trade; 6 MCU on ModusToolbox&trade; software <br />  [AN215656](https://www.infineon.com/AN215656) – PSoC&trade; 6 MCU: Dual-CPU system design 
Code examples  | [Using ModusToolbox&trade; software](https://github.com/Infineon/Code-Examples-for-ModusToolbox-Software) on GitHub
Device documentation | [PSoC&trade; 6 MCU datasheets](https://documentation.infineon.com/html/psoc6/bnm1651211483724.html) <br /> [PSoC&trade; 6 technical reference manuals](https://documentation.infineon.com/html/psoc6/zrs1651212645947.html)
Development kits | Select your kits from the [evaluation board finder](https://www.infineon.com/cms/en/design-support/finder-selection-tools/product-finder/evaluation-board)
Libraries on GitHub  | [mtb-pdl-cat1](https://github.com/Infineon/mtb-pdl-cat1) – PSoC&trade; 6 Peripheral Driver Library (PDL)  <br /> [mtb-hal-cat1](https://github.com/Infineon/mtb-hal-cat1) – Hardware Abstraction Layer (HAL) library <br /> [retarget-io](https://github.com/Infineon/retarget-io) – Utility library to retarget STDIO messages to a UART port 
Middleware on GitHub  | [psoc6-middleware](https://github.com/Infineon/modustoolbox-software#psoc-6-middleware-libraries) – Links to all PSoC&trade; 6 MCU middleware
Tools  | [Eclipse IDE for ModusToolbox&trade; software](https://www.infineon.com/modustoolbox) – ModusToolbox&trade; software is a collection of easy-to-use software and tools enabling rapid development with Infineon MCUs, covering applications from embedded sense and control to wireless and cloud-connected systems using AIROC&trade; Wi-Fi and Bluetooth&reg; connectivity devices. 

<br />

## Other resources

Infineon provides a wealth of data at www.infineon.com to help you select the right device, and quickly and effectively integrate it into your design.

For PSoC&trade; 6 MCU devices, see [How to design with PSoC&trade; 6 MCU - KBA223067](https://community.infineon.com/docs/DOC-14644) in the Infineon Developer community.


## Document history

Document title: *CE229112* - *TCP client*

 Version | Description of change
 ------- | ---------------------
 1.0.0   | New code example
 1.1.0   | Updated for ModusToolbox&trade; 2.1 <br />Code updated to use Secure Sockets and Wi-Fi connection manager libraries
 1.2.0   | Makefile updated to sync with BSP changes <br />Code updated to use binary semaphore
 2.0.0   | Major update to support ModusToolbox&trade; software v2.2, added support for new kits.<br />Added soft AP Wi-Fi interface mode.<br /> This version is not backward compatible with ModusToolbox&trade; software v2.1.
 2.1.0   | Added support for new kits
 2.2.0   | Updated to support FreeRTOS v10.3.1
 3.0.0   | Major update to support ModusToolbox&trade; v3.0 and BSPs v4.X. This version is not backward compatible with previous versions of ModusToolbox&trade; software
 3.1.0   | Added support for CY8CKIT-064B0S2-4343W
 4.0.0   | Updated to use abstraction-rtos to support various RTOS environments
 4.1.0   | Added support for CY8CEVAL-062S2-CYW43022CUB
 4.2.0   | Added support for CY8CEVAL-062S2-CYW955513SDM2WLIPA


<br />


---------------------------------------------------------

© Cypress Semiconductor Corporation, 2020-2023. This document is the property of Cypress Semiconductor Corporation, an Infineon Technologies company, and its affiliates ("Cypress").  This document, including any software or firmware included or referenced in this document ("Software"), is owned by Cypress under the intellectual property laws and treaties of the United States and other countries worldwide.  Cypress reserves all rights under such laws and treaties and does not, except as specifically stated in this paragraph, grant any license under its patents, copyrights, trademarks, or other intellectual property rights.  If the Software is not accompanied by a license agreement and you do not otherwise have a written agreement with Cypress governing the use of the Software, then Cypress hereby grants you a personal, non-exclusive, nontransferable license (without the right to sublicense) (1) under its copyright rights in the Software (a) for Software provided in source code form, to modify and reproduce the Software solely for use with Cypress hardware products, only internally within your organization, and (b) to distribute the Software in binary code form externally to end users (either directly or indirectly through resellers and distributors), solely for use on Cypress hardware product units, and (2) under those claims of Cypress’s patents that are infringed by the Software (as provided by Cypress, unmodified) to make, use, distribute, and import the Software solely for use with Cypress hardware products.  Any other use, reproduction, modification, translation, or compilation of the Software is prohibited.
<br />
TO THE EXTENT PERMITTED BY APPLICABLE LAW, CYPRESS MAKES NO WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, WITH REGARD TO THIS DOCUMENT OR ANY SOFTWARE OR ACCOMPANYING HARDWARE, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  No computing device can be absolutely secure.  Therefore, despite security measures implemented in Cypress hardware or software products, Cypress shall have no liability arising out of any security breach, such as unauthorized access to or use of a Cypress product. CYPRESS DOES NOT REPRESENT, WARRANT, OR GUARANTEE THAT CYPRESS PRODUCTS, OR SYSTEMS CREATED USING CYPRESS PRODUCTS, WILL BE FREE FROM CORRUPTION, ATTACK, VIRUSES, INTERFERENCE, HACKING, DATA LOSS OR THEFT, OR OTHER SECURITY INTRUSION (collectively, "Security Breach").  Cypress disclaims any liability relating to any Security Breach, and you shall and hereby do release Cypress from any claim, damage, or other liability arising from any Security Breach.  In addition, the products described in these materials may contain design defects or errors known as errata which may cause the product to deviate from published specifications. To the extent permitted by applicable law, Cypress reserves the right to make changes to this document without further notice. Cypress does not assume any liability arising out of the application or use of any product or circuit described in this document. Any information provided in this document, including any sample design information or programming code, is provided only for reference purposes.  It is the responsibility of the user of this document to properly design, program, and test the functionality and safety of any application made of this information and any resulting product.  "High-Risk Device" means any device or system whose failure could cause personal injury, death, or property damage.  Examples of High-Risk Devices are weapons, nuclear installations, surgical implants, and other medical devices.  "Critical Component" means any component of a High-Risk Device whose failure to perform can be reasonably expected to cause, directly or indirectly, the failure of the High-Risk Device, or to affect its safety or effectiveness.  Cypress is not liable, in whole or in part, and you shall and hereby do release Cypress from any claim, damage, or other liability arising from any use of a Cypress product as a Critical Component in a High-Risk Device. You shall indemnify and hold Cypress, including its affiliates, and its directors, officers, employees, agents, distributors, and assigns harmless from and against all claims, costs, damages, and expenses, arising out of any claim, including claims for product liability, personal injury or death, or property damage arising from any use of a Cypress product as a Critical Component in a High-Risk Device. Cypress products are not intended or authorized for use as a Critical Component in any High-Risk Device except to the limited extent that (i) Cypress’s published data sheet for the product explicitly states Cypress has qualified the product for use in a specific High-Risk Device, or (ii) Cypress has given you advance written authorization to use the product as a Critical Component in the specific High-Risk Device and you have signed a separate indemnification agreement.
<br />
Cypress, the Cypress logo, and combinations thereof, WICED, ModusToolbox, PSoC, CapSense, EZ-USB, F-RAM, and Traveo are trademarks or registered trademarks of Cypress or a subsidiary of Cypress in the United States or in other countries. For a more complete list of Cypress trademarks, visit www.infineon.com. Other names and brands may be claimed as property of their respective owners.
