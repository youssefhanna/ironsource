package
{
  import flash.geom.Point;
  import flash.geom.Rectangle;

  public class Const {
    static public const EPS : Number = 1e-14;
    static public const PI : Number = Math.PI;
    static public const PI_12 : Number = 0.5 * Math.PI;
    static public const PI_2 : Number = 2.0 * Math.PI;
    static public const PI_32 : Number = 3.0 / 2.0 * Math.PI;
    static public const EMPTY_RECT : Rectangle = new Rectangle( 0, 0, 0, 0 );
    static public const EMPTY_POINT : Point = new Point( 0, 0 );
    static public const EMPTY_VECTOR_STRING : Vector.<String> = new Vector.<String>;
    static public const EMPTY_STRING : String = "";
    static public const EMPTY_OBJECT : Object = { };
    static public function NOP() : void { }
  }
}
