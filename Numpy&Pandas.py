{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SharmilaNakka/base/blob/main/Numpy%26Pandas.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DA-Pjo2nx4cW",
        "outputId": "e8b2a952-099e-483b-ba30-245f65e98046"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[10, 10, 10]\n",
            "[10, 10, 10]\n",
            "[10, 10, 10]\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "X = [[1,2,3],\n",
        "    [4 ,5,6],\n",
        "    [7 ,8,9]]\n",
        "\n",
        "Y = [[9,8,7],\n",
        "    [6,5,4],\n",
        "    [3,2,1]]\n",
        "\n",
        "\n",
        "result = [[0,0,0],\n",
        "        [0,0,0],\n",
        "        [0,0,0]]\n",
        "\n",
        "# iterate through rows\n",
        "for i in range(len(X)):\n",
        "# iterate through columns\n",
        "    for j in range(len(X[0])):\n",
        "        result[i][j] = X[i][j] + Y[i][j]\n",
        "\n",
        "for r in result:\n",
        "    print(r)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "wO7DQ4cfo3WN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "JM7hhVkarElX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "nFEZFpK0rHH9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "S-yZIw2bvk1v"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "tLFBT320sKkg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "rFh2HXBW9fS7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "S5hljx0yB82j"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "gowGhdkf_tRp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "qDg7RSSSAnzo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "arr=np.array([1,2,3,4,5])\n",
        "print(arr)\n",
        "a=np.zeros((3,3),dtype=int)\n",
        "print(a)\n",
        "b=np.ones((2,2),dtype=int)\n",
        "print(b)\n",
        "a_range=np.arange(10)\n",
        "print(a_range)\n",
        "reshaped_arr=arr.reshape(5,1)\n",
        "print(reshaped_arr)\n",
        "sliced_arr=arr[2:4]\n",
        "print(sliced_arr)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5nuZ5Lob7iP5",
        "outputId": "9cd15681-bb70-4e4a-dc2c-6bb0948205b4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 2 3 4 5]\n",
            "[[0 0 0]\n",
            " [0 0 0]\n",
            " [0 0 0]]\n",
            "[[1 1]\n",
            " [1 1]]\n",
            "[0 1 2 3 4 5 6 7 8 9]\n",
            "[[1]\n",
            " [2]\n",
            " [3]\n",
            " [4]\n",
            " [5]]\n",
            "[3 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "arr1=np.array([1,2,3,4,5])\n",
        "print(arr1)\n",
        "arr2=np.array([3,4,5,6,7])\n",
        "print(arr2)\n",
        "result=arr1+arr2\n",
        "print(result)\n",
        "arr1=np.array([1,2,3,4,5])\n",
        "print(arr1)\n",
        "b=arr1+3\n",
        "print(b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l1uFBrWPAdJQ",
        "outputId": "855eec6b-c98c-43bf-e2f9-649b1c0232a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 2 3 4 5]\n",
            "[3 4 5 6 7]\n",
            "[ 4  6  8 10 12]\n",
            "[1 2 3 4 5]\n",
            "[4 5 6 7 8]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a1=np.array([1,2,3,4,5])\n",
        "print(a1)\n",
        "a2=np.array([3,4,5,6,7])\n",
        "print(a2)\n",
        "a3=np.vstack(a1+a2)\n",
        "print(a3)\n",
        "a1=np.array([1,2,3,4,5])\n",
        "print(a1)\n",
        "a2=np.array([3,4,5,6,7])\n",
        "print(a2)\n",
        "a3=np.stack(a1+a2)\n",
        "print(a3)\n",
        "c=np.array([1,2,3,4,5,6,7,8])\n",
        "b=np.split(c,4)\n",
        "print(b)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AxgVuv-nCdQG",
        "outputId": "6fd090d8-4c67-4957-b4a2-a8e79ba28e6c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 2 3 4 5]\n",
            "[3 4 5 6 7]\n",
            "[[ 4]\n",
            " [ 6]\n",
            " [ 8]\n",
            " [10]\n",
            " [12]]\n",
            "[1 2 3 4 5]\n",
            "[3 4 5 6 7]\n",
            "[ 4  6  8 10 12]\n",
            "[array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8])]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a1=np.array([[1,2,3,4],[5,6,7,8]])\n",
        "print(a1)\n",
        "b=a1.T\n",
        "print(b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kzvk2eK8Ig-W",
        "outputId": "56e6b540-2244-4b43-fafb-30833d69347c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3 4]\n",
            " [5 6 7 8]]\n",
            "[[1 5]\n",
            " [2 6]\n",
            " [3 7]\n",
            " [4 8]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "b1=np.array([[1,2],[3,4]])\n",
        "print(b1)\n",
        "b2=np.array([[5,6],[7,8]])\n",
        "print(b2)\n",
        "c1=np.dot(b1,b2)\n",
        "print(c1)\n",
        "d1=np.linalg.eig(c1)\n",
        "print(d1)\n",
        "e1=np.array([[1,2,3],[4,5,6]])\n",
        "print(e1)\n",
        "e2=np.array([[1,2,3],[4,5,6]])\n",
        "print(e2)\n",
        "e3=np.sum(e1+e2)\n",
        "print(e3)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ABOfc7XgJqOE",
        "outputId": "60362d23-c3c5-4a06-aba6-55140ff32b7e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2]\n",
            " [3 4]]\n",
            "[[5 6]\n",
            " [7 8]]\n",
            "[[19 22]\n",
            " [43 50]]\n",
            "(array([5.80198014e-02, 6.89419802e+01]), array([[-0.75781077, -0.40313049],\n",
            "       [ 0.65247439, -0.91514251]]))\n",
            "[[1 2 3]\n",
            " [4 5 6]]\n",
            "[[1 2 3]\n",
            " [4 5 6]]\n",
            "42\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "e1=np.array([[1,2,3],[4,5,6]])\n",
        "print(e1)\n",
        "e4=np.sum(e1,axis=0)\n",
        "print(e4)\n",
        "e5=np.sum(e1,axis=1)\n",
        "print(e5)\n",
        "arr11=np.array([1,2,3,4,5])\n",
        "print(arr11)\n",
        "arr22=np.mean(arr11)\n",
        "print(arr22)\n",
        "arr33=np.median(arr11)\n",
        "print(arr33)\n",
        "arr44=np.var(arr11)\n",
        "print(arr44)\n",
        "arr55=np.std(arr11)\n",
        "print(arr55)\n",
        "data=np.loadtxt(\"/content/txt_a.txt\")\n",
        "print(data)\n",
        "data=np.loadtxt(\"/content/txt_a.txt\",dtype=int)\n",
        "print(data)\n",
        "data=np.savetxt(\"/content/txt_b.txt\",data)\n",
        "print(data)\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5EwFGawsgCaW",
        "outputId": "7b29ff4a-f3f3-458b-b309-01ab874eec2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1 2 3]\n",
            " [4 5 6]]\n",
            "[5 7 9]\n",
            "[ 6 15]\n",
            "[1 2 3 4 5]\n",
            "3.0\n",
            "3.0\n",
            "2.0\n",
            "1.4142135623730951\n",
            "[[1. 2. 3.]\n",
            " [4. 5. 6.]\n",
            " [7. 8. 9.]]\n",
            "[[1 2 3]\n",
            " [4 5 6]\n",
            " [7 8 9]]\n",
            "None\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-21-fe6debf76efc>:19: DeprecationWarning: loadtxt(): Parsing an integer via a float is deprecated.  To avoid this warning, you can:\n",
            "    * make sure the original data is stored as integers.\n",
            "    * use the `converters=` keyword argument.  If you only use\n",
            "      NumPy 1.23 or later, `converters=float` will normally work.\n",
            "    * Use `np.loadtxt(...).astype(np.int64)` parsing the file as\n",
            "      floating point and then convert it.  (On all NumPy versions.)\n",
            "  (Deprecated NumPy 1.23)\n",
            "  data=np.loadtxt(\"/content/txt_a.txt\",dtype=int)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "a=np.array([1,2,3,4,5,6,7,8,9,10])\n",
        "plt.plot(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "36jzBEkqvPQe",
        "outputId": "4b4e4ef3-814b-4835-e710-3249f04069e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7fc254ee2bf0>]"
            ]
          },
          "metadata": {},
          "execution_count": 24
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "T7bVCSWA74cc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "a=[\"Jwalitha\",\"Ramya\",\"Durga\",\"Jahnavi\",\"Lahari\",\"sunny\",\"Dhanush\"]\n",
        "r=pd.Series(a,index=[67,43,44,89,34,45,73])\n",
        "print(r)\n",
        "df=pd.read_csv(\"/content/netflix_revenue_updated.csv\")\n",
        "print(df)\n",
        "df=pd.read_csv(\"/content/netflix_revenue_updated.csv\",sep=\" \")\n",
        "print(df)\n",
        "df=pd.read_csv(\"/content/file1.txt\",sep=\" \")\n",
        "print(df)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nP0jAkXEsPQB",
        "outputId": "30fe7d5d-0668-46ec-f360-3d9c321a9232"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "67    Jwalitha\n",
            "43       Ramya\n",
            "44       Durga\n",
            "89     Jahnavi\n",
            "34      Lahari\n",
            "45       sunny\n",
            "73     Dhanush\n",
            "dtype: object\n",
            "          Date  Global Revenue  UCAN Streaming Revenue  \\\n",
            "0   31-03-2019      4520992000              2256851000   \n",
            "1   30-06-2019      4923116000              2501199000   \n",
            "2   30-09-2019      5244905000              2621250000   \n",
            "3   31-12-2019      5467434000              2671908000   \n",
            "4   31-03-2020      5767691000              2702776000   \n",
            "5   30-06-2020      6148286000              2839670000   \n",
            "6   30-09-2020      6435637000              2933445000   \n",
            "7   31-12-2020      6644442000              2979505000   \n",
            "8   31-03-2021      7163282000              3170972000   \n",
            "9   30-06-2021      7341777000              3234643000   \n",
            "10  30-09-2021      7483467000              3257697000   \n",
            "11  31-12-2021      7709318000              3308788000   \n",
            "12  31-03-2022      7867767000              3350424000   \n",
            "13  30-06-2022      7970141000              3537863000   \n",
            "14  30-09-2022      7925589000              3601565000   \n",
            "15  31-12-2022      7852053000              3594791000   \n",
            "16  31-03-2023      8161503000              3608645000   \n",
            "\n",
            "    EMEA Streaming Revenue  LATM Streaming Revenue  APAC Streaming Revenue  \\\n",
            "0               1233379000               630472000               319602000   \n",
            "1               1319087000               677136000               349494000   \n",
            "2               1428040000               741434000               382304000   \n",
            "3               1562561000               746392000               418121000   \n",
            "4               1723474000               793453000               483660000   \n",
            "5               1892537000               785368000               569140000   \n",
            "6               2019083000               789384000               634891000   \n",
            "7               2137158000               788522000               684609000   \n",
            "8               2343674000               836647000               762414000   \n",
            "9               2400480000               860882000               799480000   \n",
            "10              2432239000               915297000               834002000   \n",
            "11              2523426000               964150000               870705000   \n",
            "12              2561831000               998948000               916754000   \n",
            "13              2457235000              1030234000               907719000   \n",
            "14              2375814000              1023945000               889037000   \n",
            "15              2350135000              1016846000               856711000   \n",
            "16              2517641000              1070192000               933523000   \n",
            "\n",
            "    UCAN Members  EMEA  Members  LATM Members  APAC Members  UCAN ARPU  \\\n",
            "0       66633000       42542000      27547000      12141000      11.45   \n",
            "1       66501000       44229000      27890000      12942000      12.52   \n",
            "2       67114000       47355000      29380000      14485000      13.08   \n",
            "3       67662000       51778000      31417000      16233000      13.22   \n",
            "4       69969000       58734000      34318000      19835000      13.09   \n",
            "5       72904000       61483000      36068000      22492000      13.25   \n",
            "6       73081000       62242000      36324000      23504000      13.40   \n",
            "7       73936000       66698000      37537000      25492000      13.51   \n",
            "8       74384000       68508000      37894000      26853000      14.25   \n",
            "9       73951000       68696000      38658000      27875000      14.54   \n",
            "10      74024000       70500000      38988000      30051000      14.68   \n",
            "11      75215000       74036000      39961000      32632000      14.78   \n",
            "12      74579000       73733000      39610000      33719000      14.91   \n",
            "13      73283000       72966000      39624000      34799000      15.95   \n",
            "14      73387000       73534000      39936000      36228000      16.37   \n",
            "15      74296000       76729000      41699000      38023000      16.23   \n",
            "16      74398000       77373000      41249000      39478000      16.18   \n",
            "\n",
            "    EMEA ARPU  LATM  ARPU  APAC  ARPU  Netflix Streaming Memberships   \n",
            "0       10.23        7.84        9.37                       148863000  \n",
            "1       10.13        8.14        9.29                       151562000  \n",
            "2       10.40        8.63        9.29                       158334000  \n",
            "3       10.51        8.18        9.07                       167090000  \n",
            "4       10.40        8.05        8.94                       182856000  \n",
            "5       10.50        7.44        8.96                       192947000  \n",
            "6       10.88        7.27        9.20                       195151000  \n",
            "7       11.05        7.12        9.32                       203663000  \n",
            "8       11.56        7.39        9.71                       207639000  \n",
            "9       11.66        7.50        9.74                       209180000  \n",
            "10      11.65        7.86        9.60                       213563000  \n",
            "11      11.64        8.14        9.26                       221844000  \n",
            "12      11.56        8.37        9.21                       221641000  \n",
            "13      11.17        8.67        8.83                       220672000  \n",
            "14      10.81        8.58        8.34                       223085000  \n",
            "15      10.43        8.30        7.69                       230747000  \n",
            "16      10.89        8.60        8.03                       232498000  \n",
            "                                          Date,Global  Revenue,UCAN  \\\n",
            "0   31-03-2019,4520992000,2256851000,1233379000,63...           NaN   \n",
            "1   30-06-2019,4923116000,2501199000,1319087000,67...           NaN   \n",
            "2   30-09-2019,5244905000,2621250000,1428040000,74...           NaN   \n",
            "3   31-12-2019,5467434000,2671908000,1562561000,74...           NaN   \n",
            "4   31-03-2020,5767691000,2702776000,1723474000,79...           NaN   \n",
            "5   30-06-2020,6148286000,2839670000,1892537000,78...           NaN   \n",
            "6   30-09-2020,6435637000,2933445000,2019083000,78...           NaN   \n",
            "7   31-12-2020,6644442000,2979505000,2137158000,78...           NaN   \n",
            "8   31-03-2021,7163282000,3170972000,2343674000,83...           NaN   \n",
            "9   30-06-2021,7341777000,3234643000,2400480000,86...           NaN   \n",
            "10  30-09-2021,7483467000,3257697000,2432239000,91...           NaN   \n",
            "11  31-12-2021,7709318000,3308788000,2523426000,96...           NaN   \n",
            "12  31-03-2022,7867767000,3350424000,2561831000,99...           NaN   \n",
            "13  30-06-2022,7970141000,3537863000,2457235000,10...           NaN   \n",
            "14  30-09-2022,7925589000,3601565000,2375814000,10...           NaN   \n",
            "15  31-12-2022,7852053000,3594791000,2350135000,10...           NaN   \n",
            "16  31-03-2023,8161503000,3608645000,2517641000,10...           NaN   \n",
            "\n",
            "    Streaming  Revenue,EMEA  Streaming.1  Revenue,LATM  Streaming.2  \\\n",
            "0         NaN           NaN          NaN           NaN          NaN   \n",
            "1         NaN           NaN          NaN           NaN          NaN   \n",
            "2         NaN           NaN          NaN           NaN          NaN   \n",
            "3         NaN           NaN          NaN           NaN          NaN   \n",
            "4         NaN           NaN          NaN           NaN          NaN   \n",
            "5         NaN           NaN          NaN           NaN          NaN   \n",
            "6         NaN           NaN          NaN           NaN          NaN   \n",
            "7         NaN           NaN          NaN           NaN          NaN   \n",
            "8         NaN           NaN          NaN           NaN          NaN   \n",
            "9         NaN           NaN          NaN           NaN          NaN   \n",
            "10        NaN           NaN          NaN           NaN          NaN   \n",
            "11        NaN           NaN          NaN           NaN          NaN   \n",
            "12        NaN           NaN          NaN           NaN          NaN   \n",
            "13        NaN           NaN          NaN           NaN          NaN   \n",
            "14        NaN           NaN          NaN           NaN          NaN   \n",
            "15        NaN           NaN          NaN           NaN          NaN   \n",
            "16        NaN           NaN          NaN           NaN          NaN   \n",
            "\n",
            "    Revenue,APAC  Streaming.3  Revenue,UCAN.1  ...  Members,UCAN  ARPU,EMEA  \\\n",
            "0            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "1            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "2            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "3            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "4            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "5            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "6            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "7            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "8            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "9            NaN          NaN             NaN  ...           NaN        NaN   \n",
            "10           NaN          NaN             NaN  ...           NaN        NaN   \n",
            "11           NaN          NaN             NaN  ...           NaN        NaN   \n",
            "12           NaN          NaN             NaN  ...           NaN        NaN   \n",
            "13           NaN          NaN             NaN  ...           NaN        NaN   \n",
            "14           NaN          NaN             NaN  ...           NaN        NaN   \n",
            "15           NaN          NaN             NaN  ...           NaN        NaN   \n",
            "16           NaN          NaN             NaN  ...           NaN        NaN   \n",
            "\n",
            "    ARPU,LATM  Unnamed: 17  ARPU,APAC  Unnamed: 19  ARPU,Netflix  Streaming.4  \\\n",
            "0         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "1         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "2         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "3         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "4         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "5         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "6         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "7         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "8         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "9         NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "10        NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "11        NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "12        NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "13        NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "14        NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "15        NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "16        NaN          NaN        NaN          NaN           NaN          NaN   \n",
            "\n",
            "    Memberships  Unnamed: 23  \n",
            "0           NaN          NaN  \n",
            "1           NaN          NaN  \n",
            "2           NaN          NaN  \n",
            "3           NaN          NaN  \n",
            "4           NaN          NaN  \n",
            "5           NaN          NaN  \n",
            "6           NaN          NaN  \n",
            "7           NaN          NaN  \n",
            "8           NaN          NaN  \n",
            "9           NaN          NaN  \n",
            "10          NaN          NaN  \n",
            "11          NaN          NaN  \n",
            "12          NaN          NaN  \n",
            "13          NaN          NaN  \n",
            "14          NaN          NaN  \n",
            "15          NaN          NaN  \n",
            "16          NaN          NaN  \n",
            "\n",
            "[17 rows x 24 columns]\n",
            "   file1\n",
            "0  file2\n",
            "1  file3\n",
            "2  file4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "WU4AeyVs7jeU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_excel(\"/content/salesworkload.xlsx\",sheet_name=1)\n",
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1UNoZEzd0sps",
        "outputId": "157f64ce-1868-4bd5-83da-fdd6c80b77e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Unnamed: 0             Unnamed: 1       Unnamed: 2 Unnamed: 3  \\\n",
            "0         NaN                    NaN              NaN        NaN   \n",
            "1         NaN                    NaN              NaN        NaN   \n",
            "2         NaN                    NaN              NaN        NaN   \n",
            "3         NaN                    NaN              NaN        NaN   \n",
            "4          id             Store name           Region     Scheme   \n",
            "5       88253       88253 London (I)   United Kingdom     Type A   \n",
            "6       38976       38976 Manchester   United Kingdom     Type A   \n",
            "7       17647        17647 Liverpool   United Kingdom     Type A   \n",
            "8       22117       22117 Birmingham   United Kingdom     Type A   \n",
            "9       73949        73949 Leicester   United Kingdom     Type B   \n",
            "10      18808      18808 London (II)   United Kingdom     Type B   \n",
            "11      71991       71991 Warsaw (I)           Poland     Type A   \n",
            "12      86208      86208 Warsaw (II)           Poland     Type B   \n",
            "13      23623           23623 Poznan           Poland     Type A   \n",
            "14      19769           19769 Krakow           Poland     Type A   \n",
            "15      15552        15552 Amsterdam  The Netherlands     Type A   \n",
            "16      95434         95434 Den Haag  The Netherlands     Type B   \n",
            "17      93033        93033 Rotterdam  The Netherlands     Type A   \n",
            "18      85321        85321 Groningen  The Netherlands     Type A   \n",
            "19      38560       38560 Prague (I)   Czech Republic     Type A   \n",
            "20      20891             20891 Brno   Czech Republic     Type A   \n",
            "21      45583          45583 Ostrava   Czech Republic     Type A   \n",
            "22      85696      85696 Prague (II)   Czech Republic     Type B   \n",
            "23      32949   32949 Copenhagen (I)          Denmark     Type A   \n",
            "24      96857  96857 Copenhagen (II)          Denmark     Type A   \n",
            "25      87703      87703 Aalborg (I)          Denmark     Type A   \n",
            "26      19000     19000 Aalborg (II)          Denmark     Type B   \n",
            "27      88994       88994 Madrid (I)            Spain     Type A   \n",
            "28      20166      20166 Madrid (II)            Spain     Type A   \n",
            "29      16927    16927 Barcelona (I)            Spain     Type A   \n",
            "30      96493   96493 Barcelona (II)            Spain     Type A   \n",
            "31      88750           88750 Bilbao            Spain     Type A   \n",
            "32      78450         78450 Rome (I)            Italy     Type B   \n",
            "33      94153        94153 Rome (II)            Italy     Type A   \n",
            "34      64983           64983 Milano            Italy     Type C   \n",
            "35      77348          77348 Bologna            Italy     Type B   \n",
            "36      78325           78325 Napoli            Italy     Type A   \n",
            "37      83160       83160 Berlin (I)          Germany     Type A   \n",
            "38      12227      12227 Berlin (II)          Germany     Type A   \n",
            "39      94882           94882 Munich          Germany     Type B   \n",
            "40      34378          34378 Hamburg          Germany     Type A   \n",
            "41      42367        42367 Frankfurt          Germany     Type A   \n",
            "42      86089          86089 Cologne          Germany     Type A   \n",
            "43      98422        98422 Paris (I)           France     Type B   \n",
            "44      79785       79785 Paris (II)           France     Type B   \n",
            "45      63354        63354 Marseille           France     Type A   \n",
            "46      85124             85124 Lyon           France     Type B   \n",
            "47      73422         73422 Bordeaux           France     Type A   \n",
            "48      91973           91973 Nantes           France     Type B   \n",
            "49      19340     19340 Brussels (I)          Belgium     Type A   \n",
            "50      76852    76852 Brussels (II)          Belgium     Type A   \n",
            "51      73762          73762 Antwerp          Belgium     Type A   \n",
            "52      81473        81473 Stockholm           Sweden     Type A   \n",
            "53      90992            90992 Malmö           Sweden     Type A   \n",
            "54      29650       29650 Gothenburg           Sweden     Type A   \n",
            "\n",
            "        Unnamed: 4  Unnamed: 5  Unnamed: 6  Unnamed: 7  Unnamed: 8  \\\n",
            "0              NaN         NaN         NaN         NaN         NaN   \n",
            "1              NaN         NaN         NaN         NaN         NaN   \n",
            "2   Month-by-month         NaN         NaN         NaN         NaN   \n",
            "3          10.2016     11.2016     12.2016      1.2017      2.2017   \n",
            "4               10     11.0000     12.0000      1.0000      2.0000   \n",
            "5              382    367.0000    350.0000    382.0000    352.0000   \n",
            "6              382    367.0000    350.0000    382.0000    352.0000   \n",
            "7              382    367.0000    350.0000    382.0000    352.0000   \n",
            "8              382    367.0000    350.0000    382.0000    352.0000   \n",
            "9              342    342.0000    313.0000    342.0000    314.0000   \n",
            "10             342    342.0000    313.0000    342.0000    314.0000   \n",
            "11             382    367.0000    350.0000    382.0000    352.0000   \n",
            "12             354    354.0000    325.0000    354.0000    326.0000   \n",
            "13             382    367.0000    350.0000    382.0000    352.0000   \n",
            "14             382    367.0000    350.0000    382.0000    352.0000   \n",
            "15             382    367.0000    350.0000    382.0000    352.0000   \n",
            "16             366    366.0000    337.0000    366.0000    338.0000   \n",
            "17             382    367.0000    350.0000    382.0000    352.0000   \n",
            "18             382    367.0000    350.0000    382.0000    352.0000   \n",
            "19             382    367.0000    350.0000    382.0000    352.0000   \n",
            "20             382    367.0000    350.0000    382.0000    352.0000   \n",
            "21             382    367.0000    350.0000    382.0000    352.0000   \n",
            "22             354    354.0000    325.0000    354.0000    326.0000   \n",
            "23             382    367.0000    350.0000    382.0000    352.0000   \n",
            "24             382    367.0000    350.0000    382.0000    352.0000   \n",
            "25             382    367.0000    350.0000    382.0000    352.0000   \n",
            "26             378    378.0000    349.0000    378.0000    350.0000   \n",
            "27             382    367.0000    350.0000    382.0000    352.0000   \n",
            "28             382    367.0000    350.0000    382.0000    352.0000   \n",
            "29             382    367.0000    350.0000    382.0000    352.0000   \n",
            "30             382    367.0000    350.0000    382.0000    352.0000   \n",
            "31             382    367.0000    350.0000    382.0000    352.0000   \n",
            "32             354    354.0000    325.0000    354.0000    326.0000   \n",
            "33             382    367.0000    350.0000    382.0000    352.0000   \n",
            "34             366    352.0000    335.0000    366.0000    337.0000   \n",
            "35             354    354.0000    325.0000    354.0000    326.0000   \n",
            "36             382    367.0000    350.0000    382.0000    352.0000   \n",
            "37             382    367.0000    350.0000    382.0000    352.0000   \n",
            "38             382    367.0000    350.0000    382.0000    352.0000   \n",
            "39             342    342.0000    313.0000    342.0000    314.0000   \n",
            "40             382    367.0000    350.0000    382.0000    352.0000   \n",
            "41             382    367.0000    350.0000    382.0000    352.0000   \n",
            "42             382    367.0000    350.0000    382.0000    352.0000   \n",
            "43             354    354.0000    325.0000    354.0000    326.0000   \n",
            "44             354    354.0000    325.0000    354.0000    326.0000   \n",
            "45             382    367.0000    350.0000    382.0000    352.0000   \n",
            "46             354    354.0000    325.0000    354.0000    326.0000   \n",
            "47             382    367.0000    350.0000    382.0000    352.0000   \n",
            "48             354    354.0000    325.0000    354.0000    326.0000   \n",
            "49             382    367.0000    350.0000    382.0000    352.0000   \n",
            "50             382    367.0000    350.0000    382.0000    352.0000   \n",
            "51             382    367.0000    350.0000    382.0000    352.0000   \n",
            "52             382    367.0000    350.0000    382.0000    352.0000   \n",
            "53             382    367.0000    350.0000    382.0000    352.0000   \n",
            "54             382    367.0000    350.0000    382.0000    352.0000   \n",
            "\n",
            "    Unnamed: 9  ...  Unnamed: 19  Unnamed: 20  Unnamed: 21  Unnamed: 22  \\\n",
            "0          NaN  ...          NaN          NaN          NaN          NaN   \n",
            "1          NaN  ...          NaN          NaN          NaN          NaN   \n",
            "2          NaN  ...          NaN          NaN          NaN          NaN   \n",
            "3       3.2017  ...      12.2016       1.2017       2.2017       3.2017   \n",
            "4       3.0000  ...      12.0000       1.0000       2.0000       3.0000   \n",
            "5     380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "6     380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "7     380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "8     380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "9     341.0000  ...     997.0000    1339.0000    1653.0000    1994.0000   \n",
            "10    341.0000  ...     997.0000    1339.0000    1653.0000    1994.0000   \n",
            "11    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "12    353.0000  ...    1033.0000    1387.0000    1713.0000    2066.0000   \n",
            "13    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "14    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "15    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "16    365.0000  ...    1069.0000    1435.0000    1773.0000    2138.0000   \n",
            "17    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "18    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "19    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "20    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "21    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "22    353.0000  ...    1033.0000    1387.0000    1713.0000    2066.0000   \n",
            "23    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "24    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "25    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "26    377.0000  ...    1105.0000    1483.0000    1833.0000    2210.0000   \n",
            "27    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "28    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "29    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "30    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "31    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "32    353.0000  ...    1033.0000    1387.0000    1713.0000    2066.0000   \n",
            "33    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "34    364.0000  ...    1053.0000    1419.0000    1756.0000    2120.0000   \n",
            "35    353.0000  ...    1033.0000    1387.0000    1713.0000    2066.0000   \n",
            "36    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "37    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "38    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "39    341.0000  ...     997.0000    1339.0000    1653.0000    1994.0000   \n",
            "40    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "41    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "42    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "43    353.0000  ...    1033.0000    1387.0000    1713.0000    2066.0000   \n",
            "44    353.0000  ...    1033.0000    1387.0000    1713.0000    2066.0000   \n",
            "45    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "46    353.0000  ...    1033.0000    1387.0000    1713.0000    2066.0000   \n",
            "47    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "48    353.0000  ...    1033.0000    1387.0000    1713.0000    2066.0000   \n",
            "49    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "50    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "51    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "52    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "53    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "54    380.0000  ...    1099.0000    1481.0000    1833.0000    2213.0000   \n",
            "\n",
            "    Unnamed: 23  Unnamed: 24  Unnamed: 25 Unnamed: 26  Unnamed: 27  \\\n",
            "0           NaN          NaN          NaN         NaN          NaN   \n",
            "1           NaN          NaN          NaN         NaN          NaN   \n",
            "2           NaN          NaN          NaN         NaN          NaN   \n",
            "3        4.2017       5.2017       6.2017      7.2017       8.2017   \n",
            "4        4.0000       5.0000       6.0000      7.0000       8.0000   \n",
            "5     2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "6     2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "7     2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "8     2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "9     2308.0000    2636.0000    2935.0000   3291.0000    3646.0000   \n",
            "10    2308.0000    2636.0000    2935.0000   3291.0000    3646.0000   \n",
            "11    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "12    2392.0000    2732.0000    3043.0000   3411.0000    3778.0000   \n",
            "13    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "14    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "15    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "16    2476.0000    2828.0000    3151.0000   3531.0000    3910.0000   \n",
            "17    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "18    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "19    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "20    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "21    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "22    2392.0000    2732.0000    3043.0000   3411.0000    3778.0000   \n",
            "23    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "24    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "25    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "26    2560.0000    2924.0000    3259.0000   3651.0000    4042.0000   \n",
            "27    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "28    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "29    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "30    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "31    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "32    2392.0000    2732.0000    3043.0000   3411.0000    3778.0000   \n",
            "33    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "34    2457.0000    2809.0000    3130.0000   3511.0000    3890.0000   \n",
            "35    2392.0000    2732.0000    3043.0000   3411.0000    3778.0000   \n",
            "36    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "37    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "38    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "39    2308.0000    2636.0000    2935.0000   3291.0000    3646.0000   \n",
            "40    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "41    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "42    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "43    2392.0000    2732.0000    3043.0000   3411.0000    3778.0000   \n",
            "44    2392.0000    2732.0000    3043.0000   3411.0000    3778.0000   \n",
            "45    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "46    2392.0000    2732.0000    3043.0000   3411.0000    3778.0000   \n",
            "47    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "48    2392.0000    2732.0000    3043.0000   3411.0000    3778.0000   \n",
            "49    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "50    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "51    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "52    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "53    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "54    2565.0000    2932.0000    3267.0000   3664.0000    4059.0000   \n",
            "\n",
            "    Unnamed: 28  \n",
            "0           NaN  \n",
            "1           NaN  \n",
            "2           NaN  \n",
            "3        9.2017  \n",
            "4        9.0000  \n",
            "5     4426.0000  \n",
            "6     4426.0000  \n",
            "7     4426.0000  \n",
            "8     4426.0000  \n",
            "9     3974.0000  \n",
            "10    3974.0000  \n",
            "11    4426.0000  \n",
            "12    4118.0000  \n",
            "13    4426.0000  \n",
            "14    4426.0000  \n",
            "15    4426.0000  \n",
            "16    4262.0000  \n",
            "17    4426.0000  \n",
            "18    4426.0000  \n",
            "19    4426.0000  \n",
            "20    4426.0000  \n",
            "21    4426.0000  \n",
            "22    4118.0000  \n",
            "23    4426.0000  \n",
            "24    4426.0000  \n",
            "25    4426.0000  \n",
            "26    4406.0000  \n",
            "27    4426.0000  \n",
            "28    4426.0000  \n",
            "29    4426.0000  \n",
            "30    4426.0000  \n",
            "31    4426.0000  \n",
            "32    4118.0000  \n",
            "33    4426.0000  \n",
            "34    4242.0000  \n",
            "35    4118.0000  \n",
            "36    4426.0000  \n",
            "37    4426.0000  \n",
            "38    4426.0000  \n",
            "39    3974.0000  \n",
            "40    4426.0000  \n",
            "41    4426.0000  \n",
            "42    4426.0000  \n",
            "43    4118.0000  \n",
            "44    4118.0000  \n",
            "45    4426.0000  \n",
            "46    4118.0000  \n",
            "47    4426.0000  \n",
            "48    4118.0000  \n",
            "49    4426.0000  \n",
            "50    4426.0000  \n",
            "51    4426.0000  \n",
            "52    4426.0000  \n",
            "53    4426.0000  \n",
            "54    4426.0000  \n",
            "\n",
            "[55 rows x 29 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_csv(\"/content/netflix_revenue_updated.csv\",sep=\" \")\n",
        "print(df.loc[1])\n",
        "df=pd.read_csv(\"/content/file1.txt\",sep=\" \")\n",
        "print(df.loc[1])\n"
      ],
      "metadata": {
        "id": "Ara1-XIN619t",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "02fa8f3b-5888-4f0b-a9ef-fe0f70441aae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Date,Global       30-06-2019,4923116000,2501199000,1319087000,67...\n",
            "Revenue,UCAN                                                    NaN\n",
            "Streaming                                                       NaN\n",
            "Revenue,EMEA                                                    NaN\n",
            "Streaming.1                                                     NaN\n",
            "Revenue,LATM                                                    NaN\n",
            "Streaming.2                                                     NaN\n",
            "Revenue,APAC                                                    NaN\n",
            "Streaming.3                                                     NaN\n",
            "Revenue,UCAN.1                                                  NaN\n",
            "Members,EMEA                                                    NaN\n",
            "Unnamed: 11                                                     NaN\n",
            "Members,LATM                                                    NaN\n",
            "Members,APAC                                                    NaN\n",
            "Members,UCAN                                                    NaN\n",
            "ARPU,EMEA                                                       NaN\n",
            "ARPU,LATM                                                       NaN\n",
            "Unnamed: 17                                                     NaN\n",
            "ARPU,APAC                                                       NaN\n",
            "Unnamed: 19                                                     NaN\n",
            "ARPU,Netflix                                                    NaN\n",
            "Streaming.4                                                     NaN\n",
            "Memberships                                                     NaN\n",
            "Unnamed: 23                                                     NaN\n",
            "Name: 1, dtype: object\n",
            "file1    file3\n",
            "Name: 1, dtype: object\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df=pd.read_csv(\"/content/netflix_revenue_updated.csv\")\n",
        "print(df)\n",
        "a=df.head(5)\n",
        "b=df.tail(5)\n",
        "total_data=pd.concat([a,b],axis=0)\n",
        "total_data.to_csv(\"c\")\n",
        "print(total_data.groupby(['EMEA Streaming Revenue'])['LATM Streaming Revenue'].count())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R_9cyNeu8joX",
        "outputId": "15e968dc-18ba-48f0-ec7e-bc5063fe2bb4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          Date  Global Revenue  UCAN Streaming Revenue  \\\n",
            "0   31-03-2019      4520992000              2256851000   \n",
            "1   30-06-2019      4923116000              2501199000   \n",
            "2   30-09-2019      5244905000              2621250000   \n",
            "3   31-12-2019      5467434000              2671908000   \n",
            "4   31-03-2020      5767691000              2702776000   \n",
            "5   30-06-2020      6148286000              2839670000   \n",
            "6   30-09-2020      6435637000              2933445000   \n",
            "7   31-12-2020      6644442000              2979505000   \n",
            "8   31-03-2021      7163282000              3170972000   \n",
            "9   30-06-2021      7341777000              3234643000   \n",
            "10  30-09-2021      7483467000              3257697000   \n",
            "11  31-12-2021      7709318000              3308788000   \n",
            "12  31-03-2022      7867767000              3350424000   \n",
            "13  30-06-2022      7970141000              3537863000   \n",
            "14  30-09-2022      7925589000              3601565000   \n",
            "15  31-12-2022      7852053000              3594791000   \n",
            "16  31-03-2023      8161503000              3608645000   \n",
            "\n",
            "    EMEA Streaming Revenue  LATM Streaming Revenue  APAC Streaming Revenue  \\\n",
            "0               1233379000               630472000               319602000   \n",
            "1               1319087000               677136000               349494000   \n",
            "2               1428040000               741434000               382304000   \n",
            "3               1562561000               746392000               418121000   \n",
            "4               1723474000               793453000               483660000   \n",
            "5               1892537000               785368000               569140000   \n",
            "6               2019083000               789384000               634891000   \n",
            "7               2137158000               788522000               684609000   \n",
            "8               2343674000               836647000               762414000   \n",
            "9               2400480000               860882000               799480000   \n",
            "10              2432239000               915297000               834002000   \n",
            "11              2523426000               964150000               870705000   \n",
            "12              2561831000               998948000               916754000   \n",
            "13              2457235000              1030234000               907719000   \n",
            "14              2375814000              1023945000               889037000   \n",
            "15              2350135000              1016846000               856711000   \n",
            "16              2517641000              1070192000               933523000   \n",
            "\n",
            "    UCAN Members  EMEA  Members  LATM Members  APAC Members  UCAN ARPU  \\\n",
            "0       66633000       42542000      27547000      12141000      11.45   \n",
            "1       66501000       44229000      27890000      12942000      12.52   \n",
            "2       67114000       47355000      29380000      14485000      13.08   \n",
            "3       67662000       51778000      31417000      16233000      13.22   \n",
            "4       69969000       58734000      34318000      19835000      13.09   \n",
            "5       72904000       61483000      36068000      22492000      13.25   \n",
            "6       73081000       62242000      36324000      23504000      13.40   \n",
            "7       73936000       66698000      37537000      25492000      13.51   \n",
            "8       74384000       68508000      37894000      26853000      14.25   \n",
            "9       73951000       68696000      38658000      27875000      14.54   \n",
            "10      74024000       70500000      38988000      30051000      14.68   \n",
            "11      75215000       74036000      39961000      32632000      14.78   \n",
            "12      74579000       73733000      39610000      33719000      14.91   \n",
            "13      73283000       72966000      39624000      34799000      15.95   \n",
            "14      73387000       73534000      39936000      36228000      16.37   \n",
            "15      74296000       76729000      41699000      38023000      16.23   \n",
            "16      74398000       77373000      41249000      39478000      16.18   \n",
            "\n",
            "    EMEA ARPU  LATM  ARPU  APAC  ARPU  Netflix Streaming Memberships   \n",
            "0       10.23        7.84        9.37                       148863000  \n",
            "1       10.13        8.14        9.29                       151562000  \n",
            "2       10.40        8.63        9.29                       158334000  \n",
            "3       10.51        8.18        9.07                       167090000  \n",
            "4       10.40        8.05        8.94                       182856000  \n",
            "5       10.50        7.44        8.96                       192947000  \n",
            "6       10.88        7.27        9.20                       195151000  \n",
            "7       11.05        7.12        9.32                       203663000  \n",
            "8       11.56        7.39        9.71                       207639000  \n",
            "9       11.66        7.50        9.74                       209180000  \n",
            "10      11.65        7.86        9.60                       213563000  \n",
            "11      11.64        8.14        9.26                       221844000  \n",
            "12      11.56        8.37        9.21                       221641000  \n",
            "13      11.17        8.67        8.83                       220672000  \n",
            "14      10.81        8.58        8.34                       223085000  \n",
            "15      10.43        8.30        7.69                       230747000  \n",
            "16      10.89        8.60        8.03                       232498000  \n",
            "EMEA Streaming Revenue\n",
            "1233379000    1\n",
            "1319087000    1\n",
            "1428040000    1\n",
            "1562561000    1\n",
            "1723474000    1\n",
            "2350135000    1\n",
            "2375814000    1\n",
            "2457235000    1\n",
            "2517641000    1\n",
            "2561831000    1\n",
            "Name: LATM Streaming Revenue, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_csv(\"/content/netflix_revenue_updated.csv\")\n",
        "print(df)\n",
        "df=df.drop_duplicates()\n",
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xoY7uT2gAGkL",
        "outputId": "ee9cd8e7-33f1-44d6-b6ee-4a6d1c8866a0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          Date  Global Revenue  UCAN Streaming Revenue  \\\n",
            "0   31-03-2019      4520992000              2256851000   \n",
            "1   30-06-2019      4923116000              2501199000   \n",
            "2   30-09-2019      5244905000              2621250000   \n",
            "3   31-12-2019      5467434000              2671908000   \n",
            "4   31-03-2020      5767691000              2702776000   \n",
            "5   30-06-2020      6148286000              2839670000   \n",
            "6   30-09-2020      6435637000              2933445000   \n",
            "7   31-12-2020      6644442000              2979505000   \n",
            "8   31-03-2021      7163282000              3170972000   \n",
            "9   30-06-2021      7341777000              3234643000   \n",
            "10  30-09-2021      7483467000              3257697000   \n",
            "11  31-12-2021      7709318000              3308788000   \n",
            "12  31-03-2022      7867767000              3350424000   \n",
            "13  30-06-2022      7970141000              3537863000   \n",
            "14  30-09-2022      7925589000              3601565000   \n",
            "15  31-12-2022      7852053000              3594791000   \n",
            "16  31-03-2023      8161503000              3608645000   \n",
            "\n",
            "    EMEA Streaming Revenue  LATM Streaming Revenue  APAC Streaming Revenue  \\\n",
            "0               1233379000               630472000               319602000   \n",
            "1               1319087000               677136000               349494000   \n",
            "2               1428040000               741434000               382304000   \n",
            "3               1562561000               746392000               418121000   \n",
            "4               1723474000               793453000               483660000   \n",
            "5               1892537000               785368000               569140000   \n",
            "6               2019083000               789384000               634891000   \n",
            "7               2137158000               788522000               684609000   \n",
            "8               2343674000               836647000               762414000   \n",
            "9               2400480000               860882000               799480000   \n",
            "10              2432239000               915297000               834002000   \n",
            "11              2523426000               964150000               870705000   \n",
            "12              2561831000               998948000               916754000   \n",
            "13              2457235000              1030234000               907719000   \n",
            "14              2375814000              1023945000               889037000   \n",
            "15              2350135000              1016846000               856711000   \n",
            "16              2517641000              1070192000               933523000   \n",
            "\n",
            "    UCAN Members  EMEA  Members  LATM Members  APAC Members  UCAN ARPU  \\\n",
            "0       66633000       42542000      27547000      12141000      11.45   \n",
            "1       66501000       44229000      27890000      12942000      12.52   \n",
            "2       67114000       47355000      29380000      14485000      13.08   \n",
            "3       67662000       51778000      31417000      16233000      13.22   \n",
            "4       69969000       58734000      34318000      19835000      13.09   \n",
            "5       72904000       61483000      36068000      22492000      13.25   \n",
            "6       73081000       62242000      36324000      23504000      13.40   \n",
            "7       73936000       66698000      37537000      25492000      13.51   \n",
            "8       74384000       68508000      37894000      26853000      14.25   \n",
            "9       73951000       68696000      38658000      27875000      14.54   \n",
            "10      74024000       70500000      38988000      30051000      14.68   \n",
            "11      75215000       74036000      39961000      32632000      14.78   \n",
            "12      74579000       73733000      39610000      33719000      14.91   \n",
            "13      73283000       72966000      39624000      34799000      15.95   \n",
            "14      73387000       73534000      39936000      36228000      16.37   \n",
            "15      74296000       76729000      41699000      38023000      16.23   \n",
            "16      74398000       77373000      41249000      39478000      16.18   \n",
            "\n",
            "    EMEA ARPU  LATM  ARPU  APAC  ARPU  Netflix Streaming Memberships   \n",
            "0       10.23        7.84        9.37                       148863000  \n",
            "1       10.13        8.14        9.29                       151562000  \n",
            "2       10.40        8.63        9.29                       158334000  \n",
            "3       10.51        8.18        9.07                       167090000  \n",
            "4       10.40        8.05        8.94                       182856000  \n",
            "5       10.50        7.44        8.96                       192947000  \n",
            "6       10.88        7.27        9.20                       195151000  \n",
            "7       11.05        7.12        9.32                       203663000  \n",
            "8       11.56        7.39        9.71                       207639000  \n",
            "9       11.66        7.50        9.74                       209180000  \n",
            "10      11.65        7.86        9.60                       213563000  \n",
            "11      11.64        8.14        9.26                       221844000  \n",
            "12      11.56        8.37        9.21                       221641000  \n",
            "13      11.17        8.67        8.83                       220672000  \n",
            "14      10.81        8.58        8.34                       223085000  \n",
            "15      10.43        8.30        7.69                       230747000  \n",
            "16      10.89        8.60        8.03                       232498000  \n",
            "          Date  Global Revenue  UCAN Streaming Revenue  \\\n",
            "0   31-03-2019      4520992000              2256851000   \n",
            "1   30-06-2019      4923116000              2501199000   \n",
            "2   30-09-2019      5244905000              2621250000   \n",
            "3   31-12-2019      5467434000              2671908000   \n",
            "4   31-03-2020      5767691000              2702776000   \n",
            "5   30-06-2020      6148286000              2839670000   \n",
            "6   30-09-2020      6435637000              2933445000   \n",
            "7   31-12-2020      6644442000              2979505000   \n",
            "8   31-03-2021      7163282000              3170972000   \n",
            "9   30-06-2021      7341777000              3234643000   \n",
            "10  30-09-2021      7483467000              3257697000   \n",
            "11  31-12-2021      7709318000              3308788000   \n",
            "12  31-03-2022      7867767000              3350424000   \n",
            "13  30-06-2022      7970141000              3537863000   \n",
            "14  30-09-2022      7925589000              3601565000   \n",
            "15  31-12-2022      7852053000              3594791000   \n",
            "16  31-03-2023      8161503000              3608645000   \n",
            "\n",
            "    EMEA Streaming Revenue  LATM Streaming Revenue  APAC Streaming Revenue  \\\n",
            "0               1233379000               630472000               319602000   \n",
            "1               1319087000               677136000               349494000   \n",
            "2               1428040000               741434000               382304000   \n",
            "3               1562561000               746392000               418121000   \n",
            "4               1723474000               793453000               483660000   \n",
            "5               1892537000               785368000               569140000   \n",
            "6               2019083000               789384000               634891000   \n",
            "7               2137158000               788522000               684609000   \n",
            "8               2343674000               836647000               762414000   \n",
            "9               2400480000               860882000               799480000   \n",
            "10              2432239000               915297000               834002000   \n",
            "11              2523426000               964150000               870705000   \n",
            "12              2561831000               998948000               916754000   \n",
            "13              2457235000              1030234000               907719000   \n",
            "14              2375814000              1023945000               889037000   \n",
            "15              2350135000              1016846000               856711000   \n",
            "16              2517641000              1070192000               933523000   \n",
            "\n",
            "    UCAN Members  EMEA  Members  LATM Members  APAC Members  UCAN ARPU  \\\n",
            "0       66633000       42542000      27547000      12141000      11.45   \n",
            "1       66501000       44229000      27890000      12942000      12.52   \n",
            "2       67114000       47355000      29380000      14485000      13.08   \n",
            "3       67662000       51778000      31417000      16233000      13.22   \n",
            "4       69969000       58734000      34318000      19835000      13.09   \n",
            "5       72904000       61483000      36068000      22492000      13.25   \n",
            "6       73081000       62242000      36324000      23504000      13.40   \n",
            "7       73936000       66698000      37537000      25492000      13.51   \n",
            "8       74384000       68508000      37894000      26853000      14.25   \n",
            "9       73951000       68696000      38658000      27875000      14.54   \n",
            "10      74024000       70500000      38988000      30051000      14.68   \n",
            "11      75215000       74036000      39961000      32632000      14.78   \n",
            "12      74579000       73733000      39610000      33719000      14.91   \n",
            "13      73283000       72966000      39624000      34799000      15.95   \n",
            "14      73387000       73534000      39936000      36228000      16.37   \n",
            "15      74296000       76729000      41699000      38023000      16.23   \n",
            "16      74398000       77373000      41249000      39478000      16.18   \n",
            "\n",
            "    EMEA ARPU  LATM  ARPU  APAC  ARPU  Netflix Streaming Memberships   \n",
            "0       10.23        7.84        9.37                       148863000  \n",
            "1       10.13        8.14        9.29                       151562000  \n",
            "2       10.40        8.63        9.29                       158334000  \n",
            "3       10.51        8.18        9.07                       167090000  \n",
            "4       10.40        8.05        8.94                       182856000  \n",
            "5       10.50        7.44        8.96                       192947000  \n",
            "6       10.88        7.27        9.20                       195151000  \n",
            "7       11.05        7.12        9.32                       203663000  \n",
            "8       11.56        7.39        9.71                       207639000  \n",
            "9       11.66        7.50        9.74                       209180000  \n",
            "10      11.65        7.86        9.60                       213563000  \n",
            "11      11.64        8.14        9.26                       221844000  \n",
            "12      11.56        8.37        9.21                       221641000  \n",
            "13      11.17        8.67        8.83                       220672000  \n",
            "14      10.81        8.58        8.34                       223085000  \n",
            "15      10.43        8.30        7.69                       230747000  \n",
            "16      10.89        8.60        8.03                       232498000  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "VtueVMU9CAdI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_csv(\"/content/netflix_revenue_updated.csv\")\n",
        "print(df)\n"
      ],
      "metadata": {
        "id": "-y2dTTSYCF-x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n"
      ],
      "metadata": {
        "id": "beOUHlAVINv8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "nb9CBCktFOE5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "DM6cqsKfyX66"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W54I91TMGO9s",
        "outputId": "d64ec50f-fe06-4280-edf1-564f07279863"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "runs=np.array([100,50,91,78,89,25,34,19,9,10])\n",
        "w=np.array([1,0,2,0,3,7,8,9,7,5])\n",
        "plt.plot(runs,w,color=\"black\")\n",
        "plt.title(\"IndvsAus_score\")\n",
        "plt.show\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 469
        },
        "id": "4eM7rnQHYGHl",
        "outputId": "16f48736-f765-457b-c1e2-ea6b5887f4a1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<function matplotlib.pyplot.show(close=None, block=None)>"
            ]
          },
          "metadata": {},
          "execution_count": 6
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "#Generate array of 200 values between pi &pi\n",
        "tiger=np.linspace(-2*np.pi,2*np.pi,50)\n",
        "print(tiger)\n",
        "\n",
        "plt.plot(tiger,np.sin(tiger),color=\"black\")\n",
        "#plt.plot(x,y,,color,lables....)\n",
        "plt.title(\"sin(x)\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 626
        },
        "id": "eCIsQA74YWcf",
        "outputId": "5622876f-6c8b-4463-a4e6-00b439543917"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[-6.28318531 -6.02672876 -5.77027222 -5.51381568 -5.25735913 -5.00090259\n",
            " -4.74444605 -4.48798951 -4.23153296 -3.97507642 -3.71861988 -3.46216333\n",
            " -3.20570679 -2.94925025 -2.6927937  -2.43633716 -2.17988062 -1.92342407\n",
            " -1.66696753 -1.41051099 -1.15405444 -0.8975979  -0.64114136 -0.38468481\n",
            " -0.12822827  0.12822827  0.38468481  0.64114136  0.8975979   1.15405444\n",
            "  1.41051099  1.66696753  1.92342407  2.17988062  2.43633716  2.6927937\n",
            "  2.94925025  3.20570679  3.46216333  3.71861988  3.97507642  4.23153296\n",
            "  4.48798951  4.74444605  5.00090259  5.25735913  5.51381568  5.77027222\n",
            "  6.02672876  6.28318531]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, 'sin(x)')"
            ]
          },
          "metadata": {},
          "execution_count": 7
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "#creating X\n",
        "overs=np.arange(5,50,5)\n",
        "overs_a=np.arange(5,30,5)\n",
        "#creating y\n",
        "runs_i=np.array([25,51,84,131,160,189,220,250,267])\n",
        "runs_a=np.array([15,41,94,110,151])\n",
        "wickets=np.array([12,32,96])\n",
        "#plotting\n",
        "plt.subplot(2,1,2)\n",
        "plt.plot(overs,runs_i,color=\"blue\",label=\"India\")\n",
        "plt.subplot(2,1,1)\n",
        "plt.plot(overs_a,runs_a,color=\"black\",label=\"Aus\")\n",
        "plt.legend(loc=\"best\")\n",
        "#plt.subplot(2,1,2)\n",
        "#plt.subplot(2,1,1)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "G8Y3jAdVYjRK",
        "outputId": "e73606f3-7af2-41a9-913f-927abb96a8a2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.legend.Legend at 0x7cfe7b725a20>"
            ]
          },
          "metadata": {},
          "execution_count": 8
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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bBhMTU0VrrJpaHIBpeLGeIWFhbCyslK4GsNWUlICAPxlIiKqQXl5OX7++WdER0dj165d0Gg0AABnZ2e88sormD59Ojw8PBSusulpcgHF1NQU9vb2uHnzJgDpfjg891eZRqPBrVu3YG1t3eyWTyYiqo2bN2/iq6++wsqVK3H58mV5++DBgxEaGorRo0fzbvF6VOdvpgMHDuDDDz/E8ePHkZGRgW3btmH06NEApHNyc+fOxQ8//IBLly7Bzs4OgYGBWLZsmc79Zdq3b48rV67ovG9UVBTeeeedB+vNX1xcXABADilUNRMTE3h4eDDAERH9RQiBX375BdHR0diyZYt8v7PWrVtjypQpmDFjBrp06aJwlc1DnQNKQUEBevbsiZdffhljx47VaSssLMSJEycwb9489OzZE3/++Sdee+01PP300zh27JjOvosWLcK0adPk5zY2NvXsQmUqlQqurq5wcnKqdDM90rKwsICJCRcTJiLKycnB2rVrERMTg3Pnzsnb/fz8EBYWhueee47TBhpZnQNKcHAwgoODq2yzs7PDnj17dLb95z//wWOPPYb09HSdc3Q2NjbykQ59MTU15fwKIiKq1rFjxxATE4ONGzeisLAQANCyZUtMnDgRoaGh6NWrl8IVNl96/+dzbm4uVCpVpcVpli1bBkdHR/Tq1QsffvghysrK9F0KERERCgsLsWrVKvTt2xd9+/bFqlWrUFhYiO7du+PTTz/F9evXsXLlSoYThel1dmRRURHefvttTJgwQWfN/X/84x949NFH4eDggF9//RWRkZHIyMjAxx9/XOX7FBcXo7i4WH6uVqv1WTYRETVB586dw8qVK/H1118jNzcXgHSq+9lnn0VYWBj69+/POXkGRG8BpbS0FM899xyEEIiOjtZpmz17tvxnX19fWFhYYMaMGYiKiqryLo5RUVG8Iy8REdVZSUkJtm7dipiYGMTHx8vbvb29MWPGDLz00kto06aNghVSdfQSUCrCyZUrVxAbG3vfOxb6+fmhrKwMly9frnJ2dGRkpE6oUavVcHd3b/C6iYioaUhLS8Pnn3+Or776Sr6i08TEBE8//TTCwsIQGBjIiwQMXIMHlIpwcvHiRezfvx+Ojo73fU1SUhJMTEzg5ORUZbulpWWVR1aIiIgqlJeX44cffkB0dDR2794tr5bt5uaGadOm4ZVXXkG7du0U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Dh3Qpk0boxvTiIgI7Ny5E/v370e7du3k7S4uLigpKUFOTo7O/sY2htX1ryp+fn4AYFRjaGFhgY4dO6J3796IiopCz5498e9//7vJjF91/auKsY3f8ePHcfPmTTz66KMwMzODmZkZ4uPjsWLFCpiZmcHZ2dmox/B+/SsvL6/0msYeQwaUKuTn5yM1NRWurq5Kl6IXXl5ecHFxwb59++RtarUaiYmJOuePm5Jr167h9u3bRjOmQghERERg27ZtiI2NhZeXl0577969YW5urjOGycnJSE9PN4oxvF//qpKUlAQARjOGVdFoNCguLjb68atORf+qYmzjFxAQgNOnTyMpKUl+9OnTBxMnTpT/bMxjeL/+VXUqvNHHULHpuQbk9ddfF3FxcSItLU0cOnRIBAYGijZt2oibN28qXVq95eXliZMnT4qTJ08KAOLjjz8WJ0+eFFeuXBFCCLFs2TJhb28vduzYIU6dOiVGjRolvLy8xJ07dxSuvHZq6l9eXp544403REJCgkhLSxN79+4Vjz76qOjUqZMoKipSuvRaCQsLE3Z2diIuLk5kZGTIj8LCQnmf0NBQ4eHhIWJjY8WxY8eEv7+/8Pf3V7Dq2rtf/1JSUsSiRYvEsWPHRFpamtixY4fo0KGDGDhwoMKV194777wj4uPjRVpamjh16pR45513hEqlEj///LMQwrjHT4ia+9cUxq8q917VYuxjeK+7+2cIY8iAIoQYN26ccHV1FRYWFuKhhx4S48aNEykpKUqX9UD2798vAFR6TJ48WQghXWo8b9484ezsLCwtLUVAQIBITk5Wtug6qKl/hYWFYujQoaJt27bC3NxceHp6imnTponMzEyly661qvoGQKxevVre586dO+Lvf/+7aN26tbC2thZjxowRGRkZyhVdB/frX3p6uhg4cKBwcHAQlpaWomPHjuLNN98Uubm5yhZeBy+//LLw9PQUFhYWom3btiIgIEAOJ0IY9/gJUXP/msL4VeXegGLsY3ivu/tnCGOoEkKIxjlWQ0RERFQ7nINCREREBocBhYiIiAwOAwoREREZHAYUIiIiMjgMKERERGRwGFCIiIjI4DCgEBERkcFhQCEiIiKDw4BCREREBocBhYiIiAwOAwoREREZHAYUIiIiMjj/D65viOSVMy3AAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "a=[230,560,780,127,128]\n",
        "b=[200,160,270,127,400]\n",
        "years=[1,2,3,4]\n",
        "profit_a=[(a[i]-a[i-1]) for i in range(1,len(a))]\n",
        "profit_b=[(b[i]-b[i-1]) for i in range(1,len(b))]\n",
        "plt.subplot(2,1,2)\n",
        "plt.plot(years,profit_a,color=\"hotpink\",linewidth=\"3\",label=\"CompanyA\",marker=\".\",ms=\"15\",mec=\"k\")\n",
        "plt.legend(loc=\"best\")\n",
        "plt.subplot(2,1,1)\n",
        "plt.plot(years,profit_b,color=\"black\",linestyle=\"dotted\",label=\"CompanyB\",marker=\"*\")\n",
        "plt.legend(loc=\"best\")\n",
        "#plt.subplot(2,1,2)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "okajcobAYnle",
        "outputId": "7e98803d-447d-464c-93f4-635306bb01f5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.legend.Legend at 0x7cfe7b675e70>"
            ]
          },
          "metadata": {},
          "execution_count": 9
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "a=np.array([25,60,5,10])\n",
        "labe=[\"AIML\",\"python\",\"pandas\",\"Numpy\"]\n",
        "explo = [0.2,0,0,0]\n",
        "plt.pie(a,labels=labe,explode=explo,startangle=180,textprops={'fontsize':32})\n",
        "plt.show()\n",
        "plt.figure(figsize=(100, 50))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 441
        },
        "id": "cWx42P-TY9_q",
        "outputId": "c32dec4b-b77f-436f-8d0f-eb126234224c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Figure size 10000x5000 with 0 Axes>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 10000x5000 with 0 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "a=np.array([25,60,5,10])\n",
        "labe=[\"AIML\",\"python\",\"pandas\",\"Numpy\"]\n",
        "explo = [0.2,0,0,0]\n",
        "plt.pie(a,labels=labe,explode=explo,startangle=180,textprops={'fontsize':32})\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 406
        },
        "id": "Ht5atzw2ZSHd",
        "outputId": "5929c31e-b363-4095-cd4d-c0219b0bc474"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "a=np.array([25,60,5,10])\n",
        "labe=[\"AIML\",\"python\",\"pandas\",\"Numpy\"]\n",
        "plt.pie(a,labels=labe)\n",
        "co=[\"green\",\"yellow\",\"black\",\"purple\"]\n",
        "plt.pie(a,colors=co)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 406
        },
        "id": "6rLDD_c7ZkMf",
        "outputId": "f17c5d7d-5b66-468e-e3fc-ded18425dc29"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "# Load the dataset containing daily temperatures\n",
        "# Assuming the dataset is in a CSV file named 'temperature_data.csv' with a column named 'temperature'\n",
        "df = pd.read_csv('/content/city__temperature.csv')\n",
        "print(df)\n",
        "\n",
        "\n",
        "average_temperature = df['AvgTemperature'].mean()\n",
        "highest_temperature = df['AvgTemperature'].max()\n",
        "lowest_temperature = df['AvgTemperature'].min()\n",
        "threshold = 30\n",
        "days_above_threshold = df[df['AvgTemperature'] > threshold].shape[0]\n",
        "\n",
        "\n",
        "print(\"Average temperature for the month:\", average_temperature)\n",
        "print(\"Highest temperature recorded:\", highest_temperature)\n",
        "print(\"Lowest temperature recorded:\", lowest_temperature)\n",
        "print(\"Number of days where temperature exceeded\", threshold, \"degrees Celsius:\", days_above_threshold)"
      ],
      "metadata": {
        "id": "QcFqfZuiFtMz",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fc7f9dbe-6014-46ec-aca5-6b14b4b0448b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "       Region   Country  State         City  Month  Day    Year  \\\n",
            "0      Africa   Algeria    NaN      Algiers    1.0  1.0  1995.0   \n",
            "1      Africa   Algeria    NaN      Algiers    1.0  2.0  1995.0   \n",
            "2      Africa   Algeria    NaN      Algiers    1.0  3.0  1995.0   \n",
            "3      Africa   Algeria    NaN      Algiers    1.0  4.0  1995.0   \n",
            "4      Africa   Algeria    NaN      Algiers    1.0  5.0  1995.0   \n",
            "...       ...       ...    ...          ...    ...  ...     ...   \n",
            "78051  Africa  Ethiopia    NaN  Addis Ababa    1.0  5.0  1995.0   \n",
            "78052  Africa  Ethiopia    NaN  Addis Ababa    1.0  6.0  1995.0   \n",
            "78053  Africa  Ethiopia    NaN  Addis Ababa    1.0  7.0  1995.0   \n",
            "78054  Africa  Ethiopia    NaN  Addis Ababa    1.0  8.0  1995.0   \n",
            "78055  Africa  Ethiopia    NaN  Addis Ababa    NaN  NaN     NaN   \n",
            "\n",
            "       AvgTemperature  \n",
            "0                64.2  \n",
            "1                49.4  \n",
            "2                48.8  \n",
            "3                46.4  \n",
            "4                47.9  \n",
            "...               ...  \n",
            "78051            62.3  \n",
            "78052            59.3  \n",
            "78053            58.3  \n",
            "78054            57.0  \n",
            "78055             NaN  \n",
            "\n",
            "[78056 rows x 8 columns]\n",
            "Average temperature for the month: 58.70892715299664\n",
            "Highest temperature recorded: 102.8\n",
            "Lowest temperature recorded: -99.0\n",
            "Number of days where temperature exceeded 30 degrees Celsius: 70307\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "df=pd.read_csv(\"/content/plot.csv\")\n",
        "print(df)\n",
        "print(\"Least Temperature Noted in January:\\n\",df.min())\n",
        "print(\"Heightest Temperature Noted in January:\\n\",df.max())\n",
        "c=df['JAN'].mean()\n",
        "print(\"Average Temperature in the Month of January\",c)\n",
        "year = np.arange(1901,1950)\n",
        "temp=np.array([22.4,24.93,23.44,22.5,22,22.28,24.46,23.57,22.67,23.24,23.22,23.7,23.71,24.42,22.6,24.13,23.68,22.06,23.32,22.87,23.57,22.96,23.25,22.84,22.56,23.54,23.23,23.33,23.05,22.6,24.57,24.13,22.85,22.76,22.28,23.1,23.34,22.95,23.61,23.79,23.18,22.99,22.97,23.17,22.38,24.41,22.61,22.87,24.31])\n",
        "plt.plot(year,temp,color='black',label=\"x-axis=year\\ny-axis=temp\")\n",
        "plt.legend(loc='best')\n",
        "plt.title(\"Temperatures in January\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "3CzEXJzvUP7W",
        "outputId": "01f811cf-a729-418d-98a3-6994252bf1e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    YEAR    JAN Location\n",
            "0   1901  22.40       AP\n",
            "1   1902  24.93       AP\n",
            "2   1903  23.44       AP\n",
            "3   1904  22.50       AP\n",
            "4   1905  22.00       AP\n",
            "5   1906  22.28       AP\n",
            "6   1907  24.46       AP\n",
            "7   1908  23.57       AP\n",
            "8   1909  22.67       AP\n",
            "9   1910  23.24       AP\n",
            "10  1911  23.22       AP\n",
            "11  1912  23.70       AP\n",
            "12  1913  23.71       AP\n",
            "13  1914  24.42       AP\n",
            "14  1915  22.60       AP\n",
            "15  1916  24.13       AP\n",
            "16  1917  23.68       AP\n",
            "17  1918  22.06       AP\n",
            "18  1919  23.32       AP\n",
            "19  1920  22.87       AP\n",
            "20  1921  23.57       AP\n",
            "21  1922  22.96       AP\n",
            "22  1923  23.25       AP\n",
            "23  1924  22.84       AP\n",
            "24  1925  22.56       AP\n",
            "25  1926  23.54       AP\n",
            "26  1927  23.23       AP\n",
            "27  1928  23.33       AP\n",
            "28  1929  23.05       AP\n",
            "29  1930  22.60       AP\n",
            "30  1931  24.57       AP\n",
            "31  1932  24.13       AP\n",
            "32  1933  22.85       AP\n",
            "33  1934  22.76       AP\n",
            "34  1935  22.28       AP\n",
            "35  1936  23.10       AP\n",
            "36  1937  23.34       AP\n",
            "37  1938  22.95       AP\n",
            "38  1939  23.61       AP\n",
            "39  1940  23.79       AP\n",
            "40  1941  23.18       AP\n",
            "41  1942  22.99       AP\n",
            "42  1943  22.97       AP\n",
            "43  1944  23.17       AP\n",
            "44  1945  22.38       AP\n",
            "45  1946  24.41       AP\n",
            "46  1947  22.61       AP\n",
            "47  1948  22.87       AP\n",
            "48  1949  24.31       AP\n",
            "Least Temperature Noted in January:\n",
            " YEAR        1901\n",
            "JAN         22.0\n",
            "Location      AP\n",
            "dtype: object\n",
            "Heightest Temperature Noted in January:\n",
            " YEAR         1949\n",
            "JAN         24.93\n",
            "Location       AP\n",
            "dtype: object\n",
            "Average Temperature in the Month of January 23.232653061224493\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjAAAAGzCAYAAAAxPS2EAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACTY0lEQVR4nO2deXQUVfr+n+5O0umsELIRkkDYZRUREVBAQRJgFNxQFhFHBTWoOK6oo37FGQbcEEdxmTHIpg4qyCCEH7uKwACyL2EnQEiAAAnZk+76/ZFzi+qkl6ruWrvfzzk5B7qrq29XKtVPPc/73mviOI4DQRAEQRCEgTBrPQCCIAiCIAipkIAhCIIgCMJwkIAhCIIgCMJwkIAhCIIgCMJwkIAhCIIgCMJwkIAhCIIgCMJwkIAhCIIgCMJwkIAhCIIgCMJwkIAhCIIgCMJwkIAhCCLoMJlMeOutt7QeBkEQfkAChiAaYDKZRP1s2LBB66Fqxqeffoq5c+dqPQzdMGHCBERFRWk9DIIIKkK0HgBB6I358+c7/X/evHlYvXp1o8evu+46NYelKz799FPEx8djwoQJWg/FJyorKxESQpc/gjAy9BdMEA0YN26c0/+3bNmC1atXN3o8UOA4DlVVVbDZbEEzjvDwcMXfw6iUl5cjMjJS62EQhFcoQiIIH3A4HJg1axY6d+6M8PBwJCUlYdKkSbh8+bLTdq1atcKf/vQnbNiwATfeeCNsNhu6du3Kx08//vgjunbtivDwcPTs2RM7d+50ej2LJo4fP47MzExERkYiJSUFb7/9NhouJC91TKtWreLH9PnnnwMAcnJycPvttyMxMRFWqxWdOnXCnDlzGr1+//792LhxIx+nDRw4EADw1ltvwWQyNTpec+fOhclkwsmTJ0WN48qVK5gyZQrS0tJgtVrRtm1bzJgxAw6Hw2m/3377LXr27Ino6GjExMSga9eu+Oijjzz85uppWAPDxn306FFMmDABTZo0QWxsLB555BFUVFR43Z8rfvrpJwwfPhwpKSmwWq1o06YNpk2bBrvd7rTdwIED0aVLFxw4cAC33XYbIiIi0KJFC8ycOdNpO1fHEAA2bNjQKNL89ddfcf/99yM9PR1WqxVpaWl47rnnUFlZ6fRadn4dO3YMw4YNQ3R0NMaOHYs333wToaGhuHDhQqPPNXHiRDRp0gRVVVU+HReCkAsSMAThA5MmTcKLL76Ifv364aOPPsIjjzyChQsXIjMzE7W1tU7bHj16FGPGjMGdd96J6dOn4/Lly7jzzjuxcOFCPPfccxg3bhz+7//+D8eOHcOoUaMafUnb7XZkZWUhKSkJM2fORM+ePfHmm2/izTff9HlMeXl5GD16NO644w589NFHuP766wEAc+bMQcuWLfHqq6/i/fffR1paGp566il88skn/GtnzZqF1NRUdOzYEfPnz8f8+fPx2muv+XQcXY2joqICAwYMwIIFCzB+/HjMnj0b/fr1w9SpU/GXv/yFf+3q1asxevRoNG3aFDNmzMA//vEPDBw4EJs2bfJpLAAwatQoXL16FdOnT8eoUaMwd+5c/N///Z9P+5o7dy6ioqLwl7/8BR999BF69uyJN954A6+88kqjbS9fvoysrCx0794d77//Pjp27IiXX34ZK1eu9Om9Fy9ejIqKCjz55JP4+OOPkZmZiY8//hjjx49vtG1dXR0yMzORmJiI9957D/feey8eeugh1NXV4bvvvnPatqamBt9//z3uvfdecrEI7eEIgvBIdnY2J/xT+fXXXzkA3MKFC522y83NbfR4y5YtOQDc77//zj+2atUqDgBns9m4U6dO8Y9//vnnHABu/fr1/GMPP/wwB4B7+umn+cccDgc3fPhwLiwsjLtw4YLPY8rNzW30WSsqKho9lpmZybVu3drpsc6dO3MDBgxotO2bb77Jubqs5OTkcAC4EydOeB3HtGnTuMjISO7w4cNOj7/yyiucxWLh8vPzOY7juGeffZaLiYnh6urqGr2fNwBwb775ZqNx//nPf3ba7u677+aaNWvmdX8PP/wwFxkZ6fSYq2M5adIkLiIigquqquIfGzBgAAeAmzdvHv9YdXU1l5yczN177738Y66OIcdx3Pr16xudN67ee/r06ZzJZHI659j59corrzTavk+fPlzv3r2dHvvxxx8bvRdBaAU5MAQhkcWLFyM2NhZ33HEHLl68yP/07NkTUVFRWL9+vdP2nTp1Qp8+ffj/9+7dGwBw++23Iz09vdHjx48fb/SekydP5v9tMpkwefJk1NTUYM2aNT6NKSMjA5mZmY3eR1h/UlJSgosXL2LAgAE4fvw4SkpKRB8jsbgax+LFi3HrrbeiadOmTp9l8ODBsNvt+OWXXwAATZo0QXl5OVavXi3beJ544gmn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\n"
          },
          "metadata": {}
        }
      ]
    }
  ]
}
