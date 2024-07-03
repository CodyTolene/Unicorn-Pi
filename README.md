<div align="center">
  <img align="center" src=".github/images/unicorn-pi.png" />
  <h2 align="center">Unicorn-Pi</h2>
  <p align="center">
    A simple guide to setting up a Raspberry Pi Pico with the Pimoroni Unicorn Pack, including the best LED effects and animations!
  </p>
</div>

## Index <a name="index"></a>

- [Parts List](#parts-list)
- [Previews](#previews)
- [Software Setup](#software-setup)
- [Software Guide](#software-guide)
- [Licensing](#licensing)
- [Wrapping Up](#wrapping-up)

<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

## Parts List <a name="parts-list"></a>

<img src=".github/images/intro.jpeg" height="250" />

| Part                                      | Price (USD) |
| :---------------------------------------- | :---------- |
| [Raspberry Pi Pico][url-pi-pico]          | $15.00      |
| [Pimoroni Unicorn Pack][url-unicorn-pack] | $24.00      |

<p align="right">[ <a href="#index">Index</a> ]</p>

<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

## Previews <a name="previews"></a>

| Name              | Preview |
| :---------------- | :---------------------------------------------------------------- |
| Digital Clock     | ![Digital Clock](.github/images/examples/digital-clock.gif)       |
| Digital Rain      | ![Digital Rain](.github/images/examples/digital-rain.gif)         |
| DVD Bouncer       | ![DVD Bouncer](.github/images/examples/dvd-bouncer.gif)           |
| Emergency         | ![Emergency](.github/images/examples/emergency.gif)               |
| Fire              | ![Fire](.github/images/examples/fire.gif)                         |
| Fireflies         | ![Fireflies](.github/images/examples/fireflies.gif)               |
| Fireplace         | ![Fireplace](.github/images/examples/fireplace.gif)               |
| Fireworks         | ![Fireworks](.github/images/examples/fireworks.gif)               |
| Flashlight Torch  | ![Flashlight Torch](.github/images/examples/flashlight-torch.gif) |
| Lava Lamp         | ![Lava Lamp](.github/images/examples/lava-lamp.gif)               |
| Lightning         | ![Lightning](.github/images/examples/lightning.gif)               |
| Plasma            | ![Plasma](.github/images/examples/plasma.gif)                     |
| Rainbow (default) | ![Rainbow](.github/images/examples/rainbow.gif)                   |
| Raindrops         | ![Raindrops](.github/images/examples/raindrops.gif)               |
| SOS (Morse Code)  | ![SOS](.github/images/examples/sos.gif)                           |
| Snowfall          | ![Snowfall](.github/images/examples/snowfall.gif)                 |
| Warp Speed        | ![Warp Speed](.github/images/examples/warp-speed.gif)             |
| Wave              | ![Wave](.github/images/examples/wave.gif)                         |

Have another idea? Share it [here][url-new-issue]. You can also fork this repo and submit a pull request with your own effect or animation! I'd love to see what you come up with.

<p align="right">[ <a href="#index">Index</a> ]</p>

<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

## Software Setup <a name="software-setup"></a>

First make sure you have this repo cloned to your computer. If you don't have Git installed, you can download the repo as a ZIP file by clicking the green "Code" button at the top of this page. Follow the steps below to run the Python scripts in this repository on your Raspberry Pi Pico with the Pimoroni Unicorn Pack:

1. Install the Pimoroni custom software to your Raspberry Pi Pico by following the [official guide][url-pimoroni-pico-guide].
2. Download and install the Thonny IDE from the [official website][url-thonny]. 
   > ![Info][img-info] This allows us to write and run Python code on the Raspberry Pi Pico.
3. Open Thonny and connect your Raspberry Pi Pico to your computer using a USB cable.
4. On the left hand side you should see the file explorer for your Raspberry Pi Pico. Drag and drop the Python scripts from this repository into the file explorer, with `main.py` being at the top/root directory.
5. Unplug and replug your Raspberry Pi Pico to restart the device.

The file `main.py` will automatically run when the Raspberry Pi Pico is powered on.

<p align="right">[ <a href="#index">Index</a> ]</p>

<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

## Software Guide <a name="software-guide"></a>

Button layout

```bash
|==================================|
| (A) oooooooooooooooooooooooo (X) |
|     oooooooooooooooooooooooo     |
| (B) oooooooooooooooooooooooo (Y) |
|==================================|
```

| Button | Action          |
| :----- | :-------------- |
| "A"    | Previous view.  |
| "X"    | Next view.      |
| "B"    | Nothing (yet).  |
| "Y"    | Nothing (yet).  |

<p align="right">[ <a href="#index">Index</a> ]</p>

<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

## Licensing <a name="licensing"></a>

This project is licensed under the Apache License, Version 2.0. See the [APACHE_2_LICENSE](LICENSE) file for the pertaining license text.

`SPDX-License-Identifier: Apache-2.0`

<p align="right">[ <a href="#index">Index</a> ]</p>

<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

## Wrapping Up <a name="wrapping-up"></a>

Thanks to all the people and projects that made this possible! I hope you enjoy this project as much as I enjoyed working on it. If you have any questions, please let me know by opening an issue [here][url-new-issue].

| Type                                                                      | Info                                                                      |
| :------------------------------------------------------------------------ | :------------------------------------------------------------------------ |
| <img width="48" src=".github/images/ng-icons/email.svg" />                | webmaster@codytolene.com                                                  |
| <img width="48" src=".github/images/simple-icons/buymeacoffee.svg" />     | https://www.buymeacoffee.com/codytolene                                   |
| <img width="48" src=".github/images/simple-icons/bitcoin-btc-logo.svg" /> | [bc1qfx3lvspkj0q077u3gnrnxqkqwyvcku2nml86wmudy7yf2u8edmqq0a5vnt][url-btc] |

Fin. Happy programming friend!

Cody Tolene

<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->

<!-- IMAGE REFERENCES -->

[img-info]: .github/images/ng-icons/info.svg
[img-warning]: .github/images/ng-icons/warn.svg

<!-- LINK REFERENCES -->

[url-btc]: https://explorer.btc.com/btc/address/bc1qfx3lvspkj0q077u3gnrnxqkqwyvcku2nml86wmudy7yf2u8edmqq0a5vnt
[url-new-issue]: https://github.com/CodyTolene/Unicorn-Pi/issues/new
[url-pi-pico]: https://www.raspberrypi.org/products/raspberry-pi-pico/
[url-pimoroni-pico-guide]: https://learn.pimoroni.com/tutorial/pico/getting-started-with-pico
[url-thonny]: https://thonny.org/
[url-unicorn-pack]: https://shop.pimoroni.com/products/pico-unicorn-pack

<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
<!---------------------------------------------------------------------------->
